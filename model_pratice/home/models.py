from django.db import models

# Create your models here.
class Medical_library(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    causes=models.TextField(max_length=10000,null=True,blank=True)
    symptoms = models.TextField(max_length=10000,null=True,blank=True)
    diagnosis = models.TextField(max_length=10000,null=True,blank=True)
    treatment = models.TextField(max_length=10000,null=True,blank=True)

    def __str__(self):
        return self.name




