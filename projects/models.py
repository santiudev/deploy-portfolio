from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=250)
    another_link= models.CharField(max_length=250, null= True, blank=True)
    image = models.ImageField(upload_to='projects', null=True)
    

