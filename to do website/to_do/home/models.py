from pickle import TRUE
from re import T
from tabnanny import verbose
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)
    description = models.CharField(max_length=100, null = True, blank = True)
    deadline = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Task"

    
class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    context = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
    
    
  