from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path('adminindex/',views.AdminIndexView.as_view(),name="adminindex")
] 