from django.contrib import admin
from django.urls import path
from app_modules.userapp import views

app_name = "userapp"

urlpatterns = [
     path('',views.UserIndexView.as_view(),name="userindex"),
     path('about-us/',views.UserAboutusView.as_view(),name="useraboutus"),
     path('services/',views.UserServicesView.as_view(),name="services"),
     path('industries/',views.UserIndustriesView.as_view(),name="industries"),
     path('industries/<str:slug>/',views.UserIndustryDetailView.as_view(),name="industry_detail"),
     path('career/',views.UserCareerView.as_view(),name="career"),
     path('blog/',views.UserBlogView.as_view(),name="blog"),
     path('blogs/<str:slug>/',views.UserBlogDetailView.as_view(),name="blog_detail"),
     path('portfolio/',views.UserPortfolioView.as_view(),name="portfolio"),
     path('ai/',views.UserAIView.as_view(),name="ai"),
     path('ai/<str:slug>/',views.UserAIDetailView.as_view(),name="ai_detail"),
     path('contact/',views.UserContactView.as_view(),name="contact"),
     path('privacy-policy/',views.UserPrivacyPolicyView.as_view(),name="privacy_policy"),
     path('services/',views.UserServicesView.as_view(),name="services"),
     path('services/<str:slug>/',views.UserServicesDetailView.as_view(),name="services_detail"),
     path('terms-condition/',views.UserTermsConditionView.as_view(),name="terms_condition"),
     

]