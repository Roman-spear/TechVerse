from django.contrib import admin
from app_modules.adminapp import models 
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.ServiceCategory)
admin.site.register(models.ServiceDetail)
admin.site.register(models.IndustryCategory)
admin.site.register(models.Blog)
