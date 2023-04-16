from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

