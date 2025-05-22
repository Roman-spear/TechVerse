from django.db import models
from django.contrib.auth.models import AbstractUser
from app_modules.base.models import BaseModel
from django.urls import reverse

# Create your models here.


class User(AbstractUser):
    phone = models.BigIntegerField(null=True,blank=True)


class ServiceCategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name 


class AICategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name 

class IndustryCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Blog(BaseModel):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='blog_image')
    description = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=255)
    
    def __str__(self): 
        return self.title
    
class AIDetail(BaseModel):
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.header_name
    
# -------------------------------------------------------------------------------------------------------------

class ServiceDetail(BaseModel):
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.header_name
    
class ServiceOption(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_detail')
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='serviceoption_image',null=True,blank=True)
    
    def __str__(self): 
        return self.name
    
class ServiceBenefit(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_benefit')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.name
    
class ServiceProcess(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_process')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return self.name
    
class ServiceTechnology(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_technology')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.name
    
# -------------------------------------------------------------------------------------------------------------

class IndustryDetail(BaseModel):
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.header_name