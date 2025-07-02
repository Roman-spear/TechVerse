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
        context["service_category"] = models.ServiceCategory.objects.all()[:5]
        context["ai_category"] = models.AICategory.objects.all()
        context["industry_category"] = models.IndustryCategory.objects.all()
        context["blogs"] = models.Blog.objects.all().order_by('-id')[:3]
        return context
    
    
    
class UserAboutusView(TemplateView):
    template_name = "userapp/about.html"
    
class UserServicesView(TemplateView):
    template_name = "userapp/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = models.ServiceDetail.objects.all()
        return context

class UserIndustriesView(TemplateView):
    template_name = "userapp/industries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["industry_category"] = models.IndustryCategory.objects.all()
        return context
    
class UserIndustryDetailView(DetailView):
    model = models.IndustryCategory
    template_name = "userapp/industry_detail.html"
    context_object_name = "industry_data"
    slug_url_kwarg = "slug"
    slug_field = "slug"
    
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ai_category"] = models.AICategory.objects.all()
        return context
    
class UserAIDetailView(DetailView):
    model = models.AICategory
    template_name = "userapp/ai_detail.html"
    context_object_name = "ai_data"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ai_images"] = models.AIImages.objects.filter(ai_category=self.get_object()) 
        try:
            context["ai_detail"] = models.AIDetail.objects.get(ai_category=self.get_object()) 
        except:
            context["ai_detail"] = None
        context["ai_process"] = models.AIProcess.objects.filter(ai_category=self.get_object()) 
        context["ai_benefit"] = models.AIBenefit.objects.filter(ai_category=self.get_object()) 
        context["ai_service"] = models.AIServices.objects.filter(ai_category=self.get_object()) 
        print("context",context)
        return context
    

class UserBlogView(TemplateView):
    template_name = "userapp/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get('category')
        blogs = models.Blog.objects.all().order_by('-id')
        if category_id:
            category_data = models.BlogCategory.objects.get(id=category_id)
            blogs = blogs.filter(category=category_data)
        
        context["blog_category"] = models.BlogCategory.objects.all() 
        context["blogs"] = blogs
        context["category_id"] = category_id
        return context
    
    
class UserBlogDetailView(DetailView):
    model = models.Blog
    template_name = "userapp/blog_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name="data"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        print(f' ==> [Line 118]: \033[38;2;153;115;129m[data]\033[0m({type(data).__name__}) = \033[38;2;209;137;2m{data}\033[0m')
        context["related_blog"] = models.Blog.objects.exclude(id=data.id).filter(category=data.category)
        print(f' ==> [Line 119]: \033[38;2;87;50;97m[context]\033[0m({type(context).__name__}) = \033[38;2;230;139;51m{context}\033[0m')
        return context
    
    
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
    slug_url_kwarg = "slug"
    slug_field = "slug"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_option"] = models.ServiceOption.objects.filter(service_detail=self.get_object())
        context["service_benefit"] = models.ServiceBenefit.objects.filter(service_detail=self.get_object())
        context["service_process"] = models.ServiceProcess.objects.filter(service_detail=self.get_object())
        context["service_technology"] = models.ServiceTechnology.objects.filter(service_detail=self.get_object())
        return context
    

class UserTermsConditionView(TemplateView):
    template_name = "userapp/terms_condition.html"
    