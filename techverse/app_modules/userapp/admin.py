from django.contrib import admin
from app_modules.userapp import models
# Register your models here.


admin.site.register(models.CareerEnquiry)
admin.site.register(models.ContactEnquiry)