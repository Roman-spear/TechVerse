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

    def get_update_url(self):
        return reverse("adminapp:servicecategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:servicecategory_delete",kwargs={'pk':self.pk})

class AICategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name 
    
    def get_update_url(self):
        return reverse("adminapp:aicategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:aicategory_delete",kwargs={'pk':self.pk})

class IndustryCategory(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    title_description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("adminapp:industrycategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:industrycategory_delete",kwargs={'pk':self.pk})
    
class Blog(BaseModel):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='blog_image')
    description = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=255)
    
    def __str__(self): 
        return self.title
    
    def get_update_url(self):
        return reverse("adminapp:blog_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:blog_delete",kwargs={'pk':self.pk})
    
class AIDetail(BaseModel):
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = models.TextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return self.header_name
    
    def get_update_url(self):
        return reverse("adminapp:aidetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:aidetail_delete",kwargs={'pk':self.pk})
    
# ------------------------------------------------------------------------------------------------------------
    
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
        return f"{self.service_detail.header_name} - {self.name}"
    
class ServiceBenefit(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_benefit')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return f"{self.service_detail.header_name} - {self.name}"
    
class ServiceProcess(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_process')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return f"{self.service_detail.header_name} - {self.name}"
    
class ServiceTechnology(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_technology')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self): 
        return f"{self.service_detail.header_name} - {self.name}"
    
    def get_update_url(self):
        return reverse("adminapp:servicedetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:servicedetail_delete",kwargs={'pk':self.pk})
    

class IndustryDetail(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='industrydetail_image',null=True,blank=True)
    
    def __str__(self): 
        return self.name
    
    def get_update_url(self):
        return reverse("adminapp:industrydetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:industrydetail_delete",kwargs={'pk':self.pk})
    