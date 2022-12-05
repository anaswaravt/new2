from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=10)
class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    fee=models.IntegerField(max_length=100)
    def __str__(self):
        return self.name
class Staff(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name



