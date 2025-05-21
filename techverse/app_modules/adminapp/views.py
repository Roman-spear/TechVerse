from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AdminIndexView(TemplateView):
    template_name = "adminapp/index.html"