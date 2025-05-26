from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,DetailView,View,CreateView
from django.contrib import messages
from app_modules.adminapp import models
from app_modules.adminapp import forms 
from app_modules.userapp.forms import ContactEnquiryForm
from django.urls import reverse_lazy

# Create your views here.


class UserIndexView(TemplateView):
    template_name = "userapp/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_category"] = models.ServiceCategory.objects.all()
        context["ai_category"] = models.AICategory.objects.all()
        context["industry_category"] = models.IndustryCategory.objects.all()
        return context
    
    
class UserAboutusView(TemplateView):
    template_name = "userapp/about.html"
    
class UserServicesView(TemplateView):
    template_name = "userapp/services.html"

class UserIndustriesView(TemplateView):
    template_name = "userapp/industries.html"
    
class UserIndustryDetailView(DetailView):
    model = models.IndustryCategory
    template_name = "userapp/industry_detail.html"
    context_object_name = "industry_data"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["industry_detail"] = models.IndustryDetail.objects.filter(industry_category=self.get_object())
        context["industry_process"] = models.IndustryProcess.objects.filter(industry_category=self.get_object())
        return context
    
    
class UserCareerView(TemplateView):
    template_name = "userapp/career.html"
    
class UserPortfolioView(TemplateView):
    template_name = "userapp/portfolio.html"
    
class UserAIView(TemplateView):
    template_name = "userapp/ai.html"

class UserAIDetailView(DetailView):
    model = models.AICategory
    template_name = "userapp/ai_detail.html"
    context_object_name = "ai_data"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ai_images"] = models.AIImages.objects.filter(ai_category=self.get_object()) 
        try:
            context["ai_detail"] = models.AIDetail.objects.get(ai_category=self.get_object()) 
        except:
            context["ai_detail"] = None
        context["ai_process"] = models.AIProcess.objects.filter(ai_category=self.get_object()) 
        context["ai_benefit"] = models.AIBenefit.objects.filter(ai_category=self.get_object()) 
        return context
    

class UserBlogView(TemplateView):
    template_name = "userapp/blog.html"
    
class UserBlogDetailView(TemplateView):
    template_name = "userapp/blog_detail.html"
    
class UserContactView(TemplateView):
    template_name = "userapp/contact.html"
    
    def post(self,request,*args):
        form = ContactEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request,'Form submitted Successfully')
        else:
            messages.success(self.request,'Error, Please try again')
            print(form.errors)
        referer = self.request.META.get('HTTP_REFERER')
        return redirect(referer)


class UserPrivacyPolicyView(TemplateView):
    template_name = "userapp/privacy_policy.html"
    
class UserServicesDetailView(DetailView):
    model = models.ServiceDetail
    template_name = "userapp/service_detail.html"
    context_object_name = "service_data"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_option"] = models.ServiceOption.objects.filter(service_detail=self.get_object())
        context["service_benefit"] = models.ServiceBenefit.objects.filter(service_detail=self.get_object())
        context["service_process"] = models.ServiceProcess.objects.filter(service_detail=self.get_object())
        context["service_technology"] = models.ServiceTechnology.objects.filter(service_detail=self.get_object())
        return context
    

class UserTermsConditionView(TemplateView):
    template_name = "userapp/terms_condition.html"
    