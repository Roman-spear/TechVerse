from django.contrib import admin
from django.urls import path
from app_modules.adminapp import views 

app_name = "adminapp"

urlpatterns = [
    

    # --------------------------------------  USER URLS  -------------------------------------------------------
    path('user_add/', views.UserCreateView.as_view(), name="user_add"),
    path('user_list/', views.UserListView.as_view(), name="user_list"),
    path('user_update/<int:pk>/', views.UserUpdateView.as_view(), name="user_update"),
    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(), name="user_delete"),

    # --------------------------------------  SERVICECATEGORY URLS  -------------------------------------------------------
    path('servicecategory_add/', views.ServiceCategoryCreateView.as_view(), name="servicecategory_add"),
    path('servicecategory_list/', views.ServiceCategoryListView.as_view(), name="servicecategory_list"),
    path('servicecategory_update/<int:pk>/', views.ServiceCategoryUpdateView.as_view(), name="servicecategory_update"),
    path('servicecategory_delete/<int:pk>/', views.ServiceCategoryDeleteView.as_view(), name="servicecategory_delete"),
    path('servicecategoryajax/',views.ServiceCategoryDatatableView.as_view(), name='servicecategoryajax'),

    # --------------------------------------  INDUSTRYCATEGORY URLS  -------------------------------------------------------
    path('industrycategory_add/', views.IndustryCategoryCreateView.as_view(), name="industrycategory_add"),
    path('industrycategory_list/', views.IndustryCategoryListView.as_view(), name="industrycategory_list"),
    path('industrycategory_update/<int:pk>/', views.IndustryCategoryUpdateView.as_view(), name="industrycategory_update"),
    path('industrycategory_delete/<int:pk>/', views.IndustryCategoryDeleteView.as_view(), name="industrycategory_delete"),
    path('industrycategoryajax/', views.IndustryCategoryDatatableView.as_view(), name="industrycategoryajax"),

    # --------------------------------------  BLOG URLS  -------------------------------------------------------
    path('blog_add/', views.BlogCreateView.as_view(), name="blog_add"),
    path('blog_list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog_update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog_delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),


    # --------------------------------------  AICATEGORY URLS  -------------------------------------------------------
    path('aicategory_add/', views.AICategoryCreateView.as_view(), name="aicategory_add"),
    path('aicategory_list/', views.AICategoryListView.as_view(), name="aicategory_list"),
    path('aicategory_update/<int:pk>/', views.AICategoryUpdateView.as_view(), name="aicategory_update"),
    path('aicategory_delete/<int:pk>/', views.AICategoryDeleteView.as_view(), name="aicategory_delete"),


    # --------------------------------------  AIDETAIL URLS  -------------------------------------------------------
    path('aidetail_add/', views.AIDetailCreateView.as_view(), name="aidetail_add"),
    path('aidetail_list/', views.AIDetailListView.as_view(), name="aidetail_list"),
    path('aidetail_update/<int:pk>/', views.AIDetailUpdateView.as_view(), name="aidetail_update"),
    path('aidetail_delete/<int:pk>/', views.AIDetailDeleteView.as_view(), name="aidetail_delete"),
    path('aicategoryajax/',views.AiCategoryDatatableView.as_view(), name='aicategoryajax'),
    

    # --------------------------------------  SERVICEDETAIL URLS  -------------------------------------------------------
    path('servicedetail_add/', views.ServiceDetailCreateView.as_view(), name="servicedetail_add"),
    path('servicedetail_list/', views.ServiceDetailListView.as_view(), name="servicedetail_list"),
    path('servicedetail_update/<int:pk>/', views.ServiceDetailUpdateView.as_view(), name="servicedetail_update"),
    path('servicedetail_delete/<int:pk>/', views.ServiceDetailDeleteView.as_view(), name="servicedetail_delete"),

    # --------------------------------------  INDUSTRYDETAIL URLS  -------------------------------------------------------
    path('industrydetail_add/', views.IndustryDetailCreateView.as_view(), name="industrydetail_add"),
    path('industrydetail_list/', views.IndustryDetailListView.as_view(), name="industrydetail_list"),
    path('industrydetail_update/<int:pk>/', views.IndustryDetailUpdateView.as_view(), name="industrydetail_update"),
    path('industrydetail_delete/<int:pk>/', views.IndustryDetailDeleteView.as_view(), name="industrydetail_delete"),
    
    path('industry/<slug:slug>/', views.IndustryDetailView.as_view(), name="industry_detail"),

]