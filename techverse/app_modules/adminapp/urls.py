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

    # --------------------------------------  SERVICEDETAIL URLS  -------------------------------------------------------
    path('servicedetail_add/', views.ServiceDetailCreateView.as_view(), name="servicedetail_add"),
    path('servicedetail_list/', views.ServiceDetailListView.as_view(), name="servicedetail_list"),
    path('servicedetail_update/<int:pk>/', views.ServiceDetailUpdateView.as_view(), name="servicedetail_update"),
    path('servicedetail_delete/<int:pk>/', views.ServiceDetailDeleteView.as_view(), name="servicedetail_delete"),

    # --------------------------------------  INDUSTRYCATEGORY URLS  -------------------------------------------------------
    path('industrycategory_add/', views.IndustryCategoryCreateView.as_view(), name="industrycategory_add"),
    path('industrycategory_list/', views.IndustryCategoryListView.as_view(), name="industrycategory_list"),
    path('industrycategory_update/<int:pk>/', views.IndustryCategoryUpdateView.as_view(), name="industrycategory_update"),
    path('industrycategory_delete/<int:pk>/', views.IndustryCategoryDeleteView.as_view(), name="industrycategory_delete"),

    # --------------------------------------  BLOG URLS  -------------------------------------------------------
    path('blog_add/', views.BlogCreateView.as_view(), name="blog_add"),
    path('blog_list/', views.BlogListView.as_view(), name="blog_list"),
    path('blog_update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog_delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),

]