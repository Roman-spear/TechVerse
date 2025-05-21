from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class UserIndexView(TemplateView):
    template_name = "userapp/Home.html"
    
class UserAboutusView(TemplateView):
    template_name = "userapp/About.html"
    
class UserServicesView(TemplateView):
    template_name = "userapp/Services.html"

class UserIndustriesView(TemplateView):
    template_name = "userapp/Industries.html"
    
class UserCareerView(TemplateView):
    template_name = "userapp/Career.html"
    
class UserInsightsView(TemplateView):
    template_name = "userapp/Blog.html"
    
class UserPortfolioView(TemplateView):
    template_name = "userapp/Portfolio.html"
    
class UserAiDetailView(TemplateView):
    template_name = "userapp/Ai_Detail.html"
    
class UserBlogDetailView(TemplateView):
    template_name = "userapp/Blog_Detail.html"
    
class UserContactView(TemplateView):
    template_name = "userapp/Contact.html"

class UserPrivacyPolicyView(TemplateView):
    template_name = "userapp/Privacy_Policy.html"
    
class UserServicesDetailView(TemplateView):
    template_name = "userapp/Service_Detail.html"
    

class UserTermsAndConditionsView(TemplateView):
    template_name = "userapp/Terms_and_conditions.html"