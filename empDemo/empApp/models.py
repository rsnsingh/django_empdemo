from django.db import models

class Employee(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    salary=models.FloatField()
    email = models.CharField(max_length=35)
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=30)

class Contact(models.Model):
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.full_name

class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    content= models.TextField()

    def __str__(self):
        return self.full_name