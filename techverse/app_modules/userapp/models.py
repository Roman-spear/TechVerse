from django.db import models
from app_modules.base.models import BaseModel

# Create your models here.


class ContactEnquiry(BaseModel):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = models.TextField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    
class CareerEnquiry(BaseModel):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)
    position = models.CharField(max_length=255,null=True,blank=True)
    resume = models.FileField(upload_to='careerenquiry_cv',null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    