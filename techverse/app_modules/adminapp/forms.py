from django import forms
from . import models
from django_summernote.widgets import SummernoteWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        fields = "__all__"
        widgets = {
            'description': SummernoteWidget(attrs={'class': 'summernote', 'style': 'height: 300px;'})  # ✅ Valid
        }

class IndustryCategoryForm(forms.ModelForm):
    class Meta:
        model = models.IndustryCategory
        fields = "__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = "__all__"

class AICategoryForm(forms.ModelForm):
    class Meta:
        model = models.AICategory
        fields = "__all__"

class AIDetailForm(forms.ModelForm):
    class Meta:
        model = models.AIDetail
        fields = "__all__"

class ServiceDetailForm(forms.ModelForm):
    class Meta:
        model = models.ServiceDetail
        fields = "__all__"

class IndustryDetailForm(forms.ModelForm):
    class Meta:
        model = models.IndustryDetail
        fields = "__all__"
