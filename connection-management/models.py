from django.db import models

# Create your models here.
class plans(models.Model):
    planId = models.AutoField(primary_key=True)
    category = models.CharField()
    benefits = models.CharField()
    valadity = models.CharField()
    price = models.IntegerField()
