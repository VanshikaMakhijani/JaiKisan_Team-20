from django.db import models

# Create your models here.
class Farmer(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    income=models.IntegerField()
    noOfFamilyMembers=models.IntegerField()

class Field(models.Model):
    area=models.FloatField()
    soilType=models.CharField(max_length=40)
    majorCrops=models.CharField(max_length=50)
    

class FieldImage(models.Model):
    field=models.ForeignKey(Field,on_delete=models.CASCADE)
    file=models.ImageField(upload_to='uploads/')
