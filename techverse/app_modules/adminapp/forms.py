from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        fields = "__all__"

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
