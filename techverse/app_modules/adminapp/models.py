from django.db import models
from django.contrib.auth.models import AbstractUser
from app_modules.base.models import BaseModel
from django.urls import reverse
from django_summernote.fields import SummernoteTextField
# Create your models here.


class User(AbstractUser):
    phone = models.BigIntegerField(null=True,blank=True)


class ServiceCategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = SummernoteTextField(null=True,blank=True)

    def __str__(self):
        return self.name 

    def get_update_url(self):
        return reverse("adminapp:servicecategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:servicecategory_delete",kwargs={'pk':self.pk})

class AICategory(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = SummernoteTextField(null=True,blank=True)

    def __str__(self):
        return self.name 
    
    def get_update_url(self):
        return reverse("adminapp:aicategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:aicategory_delete",kwargs={'pk':self.pk})

class IndustryCategory(BaseModel):
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    title_description = SummernoteTextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("adminapp:industrycategory_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:industrycategory_delete",kwargs={'pk':self.pk})
    
class IndustryDetail(BaseModel):
    industry_category = models.ForeignKey(IndustryCategory,on_delete=models.CASCADE,related_name='industry_detail')
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True) 
    image = models.FileField(upload_to='industrydetail_image',null=True,blank=True)
    header_image = models.FileField(upload_to='industrytitle_image',null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    header_alt = models.CharField(max_length=255,null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.industry_category.name} - {self.name}"
    
    def get_update_url(self):
        return reverse("adminapp:industrydetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:industrydetail_delete",kwargs={'pk':self.pk})
    
class IndustryProcess(BaseModel):
    industry_category = models.ForeignKey(IndustryCategory,on_delete=models.CASCADE,related_name='industry_process')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True) 
    
    def __str__(self):
        return f"{self.industry_category.name} - {self.name}"
    
# --------------------------------------------------------------------------------------------------------------

class BlogCategory(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Blog(BaseModel):
    title = models.CharField(max_length=255,null=True,blank=True)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,null=True,blank=True,related_name='blog_category')
    image = models.FileField(upload_to='blog_image',null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    author = models.CharField(max_length=255,null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return self.title
    
    def get_update_url(self):
        return reverse("adminapp:blog_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:blog_delete",kwargs={'pk':self.pk})
    
class AIDetail(BaseModel):
    ai_category = models.ForeignKey(AICategory,on_delete=models.CASCADE,related_name='aidetail_category')
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = SummernoteTextField(null=True,blank=True)
    header_image = models.FileField(upload_to='industrydetail_image',null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    contact_text = models.TextField(null=True,blank=True)
    about_name = models.CharField(max_length=255,null=True,blank=True)
    about_description = SummernoteTextField()
    about_image = models.FileField(upload_to='ai_aboutimage',null=True,blank=True)
    benefit_description = SummernoteTextField()
    header_alt = models.CharField(max_length=255,null=True,blank=True)
    about_alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return self.header_name
    
    def get_update_url(self):
        return reverse("adminapp:aidetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:aidetail_delete",kwargs={'pk':self.pk})
    
class AIImages(BaseModel):
    ai_category = models.ForeignKey(AICategory,on_delete=models.CASCADE,related_name='aiimages_category')
    image = models.FileField(upload_to='ai_images',null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return self.ai_category.name
    
class AIProcess(BaseModel):
    ai_category = models.ForeignKey(AICategory,on_delete=models.CASCADE,related_name='aiprocess_category')
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField()
    
    def __str__(self): 
        return f"{self.ai_category.name} - {self.name}"
    
class AIBenefit(BaseModel):
    ai_category = models.ForeignKey(AICategory,on_delete=models.CASCADE,related_name='aibenefit_category')
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField()
    image = models.FileField(upload_to='aibenefit_image',null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return f"{self.ai_category.name} - {self.name}"
    
# ------------------------------------------------------------------------------------------------------------
    
class ServiceDetail(BaseModel):
    header_name = models.CharField(max_length=255,null=True,blank=True)
    header_description = SummernoteTextField(null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    header_image = models.FileField(upload_to='industrydetail_image',null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return self.header_name
    
class ServiceOption(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_detail')
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    image = models.FileField(upload_to='serviceoption_image',null=True,blank=True)
    alt = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self): 
        return f"{self.service_detail.header_name} - {self.name}"
    
class ServiceBenefit(BaseModel):
    service_detail = models.ForeignKey(ServiceDetail,on_delete=models.CASCADE,related_name='service_benefit')
    icon = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = SummernoteTextField(null=True,blank=True)
    
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
    description = SummernoteTextField(null=True,blank=True)
    
    def __str__(self): 
        return f"{self.service_detail.header_name} - {self.name}"
    
    def get_update_url(self):
        return reverse("adminapp:servicedetail_update",kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse("adminapp:servicedetail_delete",kwargs={'pk':self.pk})
    
