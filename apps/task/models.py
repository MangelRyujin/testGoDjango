from django.db import models

# Create your models here.
class Task(models.Model):
    STATE_CHOICES = (
        ('pendiente', 'pendiente'),
        ('progreso', 'en progreso'),
        ('completada', 'completada'),
    )
    title = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(blank=True,null=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='completada') 
    created_date_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_date_time = models.DateTimeField(auto_now=True,null=True)
  