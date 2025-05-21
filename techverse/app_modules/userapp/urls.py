from django.contrib import admin
from django.urls import path
from app_modules.userapp import views

urlpatterns = [
     path('',views.UserIndexView.as_view(),name="UserIndexView"),
     path('about-us/',views.UserAboutusView.as_view(),name="UserAboutusView"),
     path('services/',views.UserServicesView.as_view(),name="UserServicesView"),
     path('industries/',views.UserIndustriesView.as_view(),name="UserIndustriesView"),
     path('career/',views.UserCareerView.as_view(),name="UserCareerView"),
     path('blog/',views.UserInsightsView.as_view(),name="UserInsightsView"),
     path('portfolio/',views.UserPortfolioView.as_view(),name="UserPortfolioView"),
     path('ai-detail/',views.UserAiDetailView.as_view(),name="UserAiDetailView"),
     path('blog-detail/',views.UserBlogDetailView.as_view(),name="UserBlogDetailView"),
     path('contact/',views.UserContactView.as_view(),name="UserContactView"),
     path('privacy-policy/',views.UserPrivacyPolicyView.as_view(),name="UserPrivacyPolicyView"),
     path('services-detail/',views.UserServicesDetailView.as_view(),name="UserServicesDetailView"),
     path('terms_and_conditions/',views.UserTermsAndConditionsView.as_view(),name="UserTermsAndConditionsView"),
] 