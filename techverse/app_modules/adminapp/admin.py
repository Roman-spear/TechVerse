from django.contrib import admin
from app_modules.adminapp import models 
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(models.User)

admin.site.register(models.ServiceCategory)
admin.site.register(models.ServiceDetail)
admin.site.register(models.ServiceOption)
admin.site.register(models.ServiceBenefit)
admin.site.register(models.ServiceProcess)
admin.site.register(models.ServiceTechnology)

admin.site.register(models.IndustryCategory)
admin.site.register(models.IndustryDetail)
admin.site.register(models.IndustryProcess)

admin.site.register(models.AICategory)
admin.site.register(models.AIDetail)
admin.site.register(models.AIImages)
admin.site.register(models.AIBenefit)
admin.site.register(models.AIProcess)
admin.site.register(models.AIServices)

admin.site.register(models.Blog)
admin.site.register(models.BlogCategory)
