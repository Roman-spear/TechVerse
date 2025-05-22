from django.contrib import admin
from django.urls import path
from app_modules.userapp import views

app_name = "userapp"

urlpatterns = [
     path('',views.UserIndexView.as_view(),name="userindex"),
     path('useraboutus/',views.UserAboutusView.as_view(),name="useraboutus"),
     path('services/',views.UserServicesView.as_view(),name="services"),
     path('industries/',views.UserIndustriesView.as_view(),name="industries"),
     path('industry_detail/<int:pk>/',views.UserIndustryDetailView.as_view(),name="industry_detail"),
     path('career/',views.UserCareerView.as_view(),name="career"),
     path('blog/',views.UserBlogView.as_view(),name="blog"),
     path('portfolio/',views.UserPortfolioView.as_view(),name="portfolio"),
     path('ai_detail/',views.UserAiDetailView.as_view(),name="ai_detail"),
     path('blog_detail/',views.UserBlogDetailView.as_view(),name="blog_detail"),
     path('contact/',views.UserContactView.as_view(),name="contact"),
     path('privacy_policy/',views.UserPrivacyPolicyView.as_view(),name="privacy_policy"),
     path('services_detail/<int:pk>/',views.UserServicesDetailView.as_view(),name="services_detail"),
     path('terms_condition/',views.UserTermsConditionView.as_view(),name="terms_condition"),
     

]