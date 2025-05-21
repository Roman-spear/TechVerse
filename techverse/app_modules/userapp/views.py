from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,DetailView,View,CreateView
from django.contrib import messages
from app_modules.adminapp import models
from app_modules.adminapp import forms 
from django.urls import reverse_lazy

# Create your views here.


class UserIndexView(TemplateView):
    template_name = "userapp/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicecategory"] = models.ServiceCategory.objects.all()
        context["industrycategory"] = models.IndustryCategory.objects.all()
        return context
    
    
class UserAboutusView(TemplateView):
    template_name = "userapp/about.html"
    
class UserServicesView(TemplateView):
    template_name = "userapp/services.html"

class UserIndustriesView(TemplateView):
    template_name = "userapp/industries.html"
    
class UserCareerView(TemplateView):
    template_name = "userapp/career.html"
    
class UserBlogView(TemplateView):
    template_name = "userapp/blog.html"
    
class UserPortfolioView(TemplateView):
    template_name = "userapp/portfolio.html"
    
class UserAiDetailView(TemplateView):
    template_name = "userapp/ai_detail.html"
    
class UserBlogDetailView(TemplateView):
    template_name = "userapp/blog_detail.html"
    
class UserContactView(TemplateView):
    template_name = "userapp/contact.html"

class UserPrivacyPolicyView(TemplateView):
    template_name = "userapp/privacy_policy.html"
    
class UserServicesDetailView(TemplateView):
    template_name = "userapp/service_detail.html"
    

class UserTermsConditionView(TemplateView):
    template_name = "userapp/terms_condition.html"
    