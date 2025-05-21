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
    