import os
import importlib
import importlib.util
from django.core.management.base import BaseCommand

FORM_TEMPLATE_HEADER = '''from django import forms
from . import models

'''

FORM_CLASS_TEMPLATE = '''
class {model_name}Form(forms.ModelForm):
    class Meta:
        model = models.{model_name}
        fields = "__all__"
'''

URLS_HEADER_TEMPLATE = '''from django.urls import path
from . import views

urlpatterns = [
{url_patterns}
]
'''

URL_PATTERN_TEMPLATE = '''
    # --------------------------------------  {model_name_upper} URLS  -------------------------------------------------------
    path('{model_name_lower}_add/', views.{model_name}CreateView.as_view(), name="{model_name_lower}_add"),
    path('{model_name_lower}_list/', views.{model_name}ListView.as_view(), name="{model_name_lower}_list"),
    path('{model_name_lower}_update/<int:pk>/', views.{model_name}UpdateView.as_view(), name="{model_name_lower}_update"),
    path('{model_name_lower}_delete/<int:pk>/', views.{model_name}DeleteView.as_view(), name="{model_name_lower}_delete"),
'''

VIEW_TEMPLATE_HEADER = '''from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from . import models, forms

'''

VIEW_CLASS_TEMPLATE = '''
# --------------------------------------------------- {model_name_upper}-CRUD --------------------------------------------------------

class {model_name}CreateView(CreateView):
    model = models.{model_name}
    form_class = forms.{model_name}Form
    template_name = "adminapp/{model_name_lower}_add.html"
    success_url = reverse_lazy("adminapp:{model_name_lower}_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, '{model_name_upper} Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class {model_name}ListView(ListView):
    model = models.{model_name}
    template_name = "adminapp/{model_name_lower}_list.html"
    context_object_name = "{model_name_lower}_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["{model_name_lower}"] = models.{model_name}.objects.first()
        return context


class {model_name}UpdateView(UpdateView):
    model = models.{model_name}
    form_class = forms.{model_name}Form
    template_name = "adminapp/{model_name_lower}_update.html"
    success_url = reverse_lazy("adminapp:{model_name_lower}_list")

    def form_valid(self, form):
        messages.success(self.request, '{model_name_upper} Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class {model_name}DeleteView(DeleteView):
    model = models.{model_name}
    template_name = "adminapp/{model_name_lower}_list.html"
    success_url = reverse_lazy("adminapp:{model_name_lower}_list")

    def form_valid(self, form):
        messages.success(self.request, '{model_name_upper} Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)
'''

def get_app_path(app_name):
    spec = importlib.util.find_spec(app_name)
    if spec is None or not spec.origin:
        raise FileNotFoundError(f"Could not locate the app '{app_name}'")
    return os.path.dirname(spec.origin)

class Command(BaseCommand):
    help = "Generates CRUD views, forms, and urls for models in a Django app."

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Dotted path of the app (e.g., app_modules.adminapp)')

    def handle(self, *args, **options):
        app_name = options['app_name']
        if not app_name:
            self.stdout.write(self.style.ERROR("Please provide an app name"))
            return

        try:
            app_path = get_app_path(app_name)
        except FileNotFoundError as e:
            self.stdout.write(self.style.ERROR(str(e)))
            return

        try:
            models_module = importlib.import_module(f"{app_name}.models")
        except ModuleNotFoundError:
            self.stdout.write(self.style.ERROR(f"No models found in app '{app_name}'"))
            return

        model_classes = [
            cls for name, cls in models_module.__dict__.items()
            if isinstance(cls, type) and hasattr(cls, "_meta") and cls._meta.app_label == app_name.split('.')[-1]
        ]

        if not model_classes:
            self.stdout.write(self.style.ERROR(f"No models found in app '{app_name}'"))
            return

        # File paths
        forms_file = os.path.join(app_path, 'forms.py')
        views_file = os.path.join(app_path, 'views.py')
        urls_file = os.path.join(app_path, 'urls.py')

        # === FORMS ===
        existing_forms = ''
        if os.path.exists(forms_file):
            with open(forms_file, 'r') as f:
                existing_forms = f.read()

        new_form_classes = ''
        for cls in model_classes:
            if f'class {cls.__name__}Form' not in existing_forms:
                new_form_classes += FORM_CLASS_TEMPLATE.format(model_name=cls.__name__)

        with open(forms_file, 'w') as f:
            if not existing_forms:
                f.write(FORM_TEMPLATE_HEADER + new_form_classes)
            else:
                f.write(existing_forms + new_form_classes)

        # === VIEWS ===
        existing_views = ''
        if os.path.exists(views_file):
            with open(views_file, 'r') as f:
                existing_views = f.read()

        new_view_classes = ''
        for cls in model_classes:
            if f'class {cls.__name__}CreateView' not in existing_views:
                new_view_classes += VIEW_CLASS_TEMPLATE.format(
                    model_name_upper=cls.__name__.upper(),
                    model_name=cls.__name__,
                    model_name_lower=cls.__name__.lower()
                )

        with open(views_file, 'w') as f:
            if not existing_views:
                f.write(VIEW_TEMPLATE_HEADER + new_view_classes)
            else:
                f.write(existing_views + new_view_classes)

        # === URLS ===
        existing_urls = ''
        if os.path.exists(urls_file):
            with open(urls_file, 'r') as f:
                existing_urls = f.read()

        new_url_patterns = ''
        for cls in model_classes:
            if f'{cls.__name__}CreateView' not in existing_urls:
                new_url_patterns += URL_PATTERN_TEMPLATE.format(
                    model_name_upper=cls.__name__.upper(),
                    model_name=cls.__name__,
                    model_name_lower=cls.__name__.lower()
                )

        with open(urls_file, 'w') as f:
            if not existing_urls:
                f.write(URLS_HEADER_TEMPLATE.format(url_patterns=new_url_patterns))
            else:
                # insert new patterns before final closing bracket
                new_content = existing_urls.strip().rstrip(']') + new_url_patterns + '\n]'
                f.write(new_content)

        self.stdout.write(self.style.SUCCESS("CRUD scaffolding updated successfully."))
