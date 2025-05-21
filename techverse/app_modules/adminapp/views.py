from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,DetailView,View,CreateView
from django.contrib import messages
from app_modules.adminapp import models
from app_modules.adminapp import forms 
from django.urls import reverse_lazy

from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ServiceCategory
from django.utils.dateparse import parse_date
# Create your views here.

# --------------------------------------------------- USER-CRUD --------------------------------------------------------

class UserCreateView(CreateView):
    model = models.User
    form_class = forms.UserForm
    template_name = "adminapp/user_add.html"
    success_url = reverse_lazy("adminapp:user_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'USER Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class UserListView(ListView):
    model = models.User
    template_name = "adminapp/user_list.html"
    context_object_name = "user_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = models.User.objects.first()
        return context


class UserUpdateView(UpdateView):
    model = models.User
    form_class = forms.UserForm
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("adminapp:user_list")

    def form_valid(self, form):
        messages.success(self.request, 'USER Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class UserDeleteView(DeleteView):
    model = models.User
    template_name = "adminapp/user_list.html"
    success_url = reverse_lazy("adminapp:user_list")

    def form_valid(self, form):
        messages.success(self.request, 'USER Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)

# --------------------------------------------------- SERVICECATEGORY-CRUD --------------------------------------------------------

class ServiceCategoryCreateView(CreateView):
    model = models.ServiceCategory
    form_class = forms.ServiceCategoryForm
    template_name = "adminapp/servicecategory_add.html"
    success_url = reverse_lazy("adminapp:servicecategory_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'SERVICECATEGORY Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class ServiceCategoryListView(ListView):
    model = models.ServiceCategory
    template_name = "adminapp/servicecategory_list.html"
    context_object_name = "servicecategory_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicecategory"] = models.ServiceCategory.objects.first()
        return context


class ServiceCategoryUpdateView(UpdateView):
    model = models.ServiceCategory
    form_class = forms.ServiceCategoryForm
    template_name = "adminapp/servicecategory_update.html"
    success_url = reverse_lazy("adminapp:servicecategory_list")

    def form_valid(self, form):
        messages.success(self.request, 'SERVICECATEGORY Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class ServiceCategoryDeleteView(DeleteView):
    model = models.ServiceCategory
    template_name = "adminapp/servicecategory_list.html"
    success_url = reverse_lazy("adminapp:servicecategory_list")

    def form_valid(self, form):
        messages.success(self.request, 'SERVICECATEGORY Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class ServiceCategoryDatatableView(View):
    model = ServiceCategory
    queryset = ServiceCategory.objects.all().order_by('-id')
    
    def _get_actions(self, obj):
        update_url = f"/adminapp/servicecategory_update/{obj.id}/"
        return (
            f'<a href="{update_url}" title="Edit" class="btn btn-primary btn-xs">'
            '<i class="fa fa-edit"></i></a> '
            f'<a data-title="{obj.name}" title="Delete" onclick="showDeletemodal({obj.id})" '
            'data-bs-toggle="modal" class="btn btn-danger btn-xs btn-delete">'
            '<i class="fa fa-trash" style="color:white;"></i></a>'
        )
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', '')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if search:
            qs = qs.filter(Q(name__icontains=search))
        if start_date and end_date:
            start_date_parsed = parse_date(start_date)
            end_date_parsed = parse_date(end_date)
            if start_date_parsed and end_date_parsed:
                qs = qs.filter(created_at__gte=start_date_parsed, created_at__lte=end_date_parsed)
        return qs
    
    def prepare_results(self, qs, start_index):
        data = []
        for index, obj in enumerate(qs):
            data.append({
                'id': start_index + index + 1,
                'name': obj.name or '',
                'actions': self._get_actions(obj)
            })
        return data

    def get(self, request, *args, **kwargs):
        self.request = request  # Fix to allow access in filter_queryset
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))

        filtered_qs = self.filter_queryset(self.queryset)
        paginator = Paginator(filtered_qs, length)
        page_number = (start // length) + 1
        page_obj = paginator.get_page(page_number)

        data = self.prepare_results(page_obj, start)

        response = {
            'draw': int(request.GET.get('draw', 0)),
            'recordsTotal': self.queryset.count(),
            'recordsFiltered': filtered_qs.count(),
            'data': data,
        }
        return JsonResponse(response)





# --------------------------------------------------- SERVICEDETAIL-CRUD --------------------------------------------------------

class ServiceDetailCreateView(CreateView):
    model = models.ServiceDetail
    form_class = forms.ServiceDetailForm
    template_name = "adminapp/servicedetail_add.html"
    success_url = reverse_lazy("adminapp:servicedetail_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'SERVICEDETAIL Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class ServiceDetailListView(ListView):
    model = models.ServiceDetail
    template_name = "adminapp/servicedetail_list.html"
    context_object_name = "servicedetail_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicedetail"] = models.ServiceDetail.objects.first()
        return context


class ServiceDetailUpdateView(UpdateView):
    model = models.ServiceDetail
    form_class = forms.ServiceDetailForm
    template_name = "adminapp/servicedetail_update.html"
    success_url = reverse_lazy("adminapp:servicedetail_list")

    def form_valid(self, form):
        messages.success(self.request, 'SERVICEDETAIL Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class ServiceDetailDeleteView(DeleteView):
    model = models.ServiceDetail
    template_name = "adminapp/servicedetail_list.html"
    success_url = reverse_lazy("adminapp:servicedetail_list")

    def form_valid(self, form):
        messages.success(self.request, 'SERVICEDETAIL Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)

# --------------------------------------------------- INDUSTRYCATEGORY-CRUD --------------------------------------------------------

class IndustryCategoryCreateView(CreateView):
    model = models.IndustryCategory
    form_class = forms.IndustryCategoryForm
    template_name = "adminapp/industrycategory_add.html"
    success_url = reverse_lazy("adminapp:industrycategory_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'INDUSTRYCATEGORY Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class IndustryCategoryListView(ListView):
    model = models.IndustryCategory
    template_name = "adminapp/industrycategory_list.html"
    context_object_name = "industrycategory_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["industrycategory"] = models.IndustryCategory.objects.first()
        return context


class IndustryCategoryUpdateView(UpdateView):
    model = models.IndustryCategory
    form_class = forms.IndustryCategoryForm
    template_name = "adminapp/industrycategory_update.html"
    success_url = reverse_lazy("adminapp:industrycategory_list")

    def form_valid(self, form):
        messages.success(self.request, 'INDUSTRYCATEGORY Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class IndustryCategoryDeleteView(DeleteView):
    model = models.IndustryCategory
    template_name = "adminapp/industrycategory_list.html"
    success_url = reverse_lazy("adminapp:industrycategory_list")

    def form_valid(self, form):
        messages.success(self.request, 'INDUSTRYCATEGORY Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)

# --------------------------------------------------- BLOG-CRUD --------------------------------------------------------

class BlogCreateView(CreateView):
    model = models.Blog
    form_class = forms.BlogForm
    template_name = "adminapp/blog_add.html"
    success_url = reverse_lazy("adminapp:blog_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'BLOG Added Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class BlogListView(ListView):
    model = models.Blog
    template_name = "adminapp/blog_list.html"
    context_object_name = "blog_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = models.Blog.objects.first()
        return context


class BlogUpdateView(UpdateView):
    model = models.Blog
    form_class = forms.BlogForm
    template_name = "adminapp/blog_update.html"
    success_url = reverse_lazy("adminapp:blog_list")

    def form_valid(self, form):
        messages.success(self.request, 'BLOG Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)


class BlogDeleteView(DeleteView):
    model = models.Blog
    template_name = "adminapp/blog_list.html"
    success_url = reverse_lazy("adminapp:blog_list")

    def form_valid(self, form):
        messages.success(self.request, 'BLOG Deleted Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Error, Please try again')
        return super().form_invalid(form)
