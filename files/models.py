from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=30)
    file_url=models.URLField(null=False)
    date_created = models.CharField(max_length=255)
    