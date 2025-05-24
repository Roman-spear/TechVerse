from django.db import models
from app_modules.base.models import BaseModel
from django_summernote.fields import SummernoteTextField
# Create your models here.


class ContactEnquiry(BaseModel):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    company = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    subject = SummernoteTextField(null=True,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    message = SummernoteTextField(null=True,blank=True)
    
    def __str__(self):
        return self.email or "Unknown"
    
class CareerEnquiry(BaseModel):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)
    position = models.CharField(max_length=255,null=True,blank=True)
    resume = models.FileField(upload_to='careerenquiry_cv',null=True,blank=True)
    message = SummernoteTextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name or 'Unknown'} - {self.position or 'Unknown'}"