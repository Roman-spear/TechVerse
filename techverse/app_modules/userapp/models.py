from django.db import models
from app_modules.base.models import BaseModel

# Create your models here.
class ServiceCategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed Category"

class ServiceDetail(BaseModel):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='service_category')
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name or "Unnamed Service"

class Industries(BaseModel):
    title = models.CharField(max_length=255, null=True,blank=True)
    description = models.CharField(max_length=255, null=True,blank=True)
    
class IndustrieCategory(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    description = models.CharField(max_length=255, null=True,blank=True)
    
class Blog(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_img',null=True,blank=True)
    
class Career(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True,blank=True)
    cv = models.ImageField(upload_to='blog_img',null=True,blank=True)
    message = models.CharField(max_length=255, null=True,blank=True)
    
class GetInTouch(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)