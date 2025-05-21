from django.db import models
from app_modules.base.models import BaseModel

# Create your models here.


class ContactEnquiry(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.BigIntegerField()
    