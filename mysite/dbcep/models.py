from email.policy import default
from unicodedata import name
from attr import define
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Hotel_Branches(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=20,null=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservation',args=[self.id])

class Employees(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=100,null=False)
    gender=models.CharField(max_length=10,null=False)
    salary = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    dateofbirth = models.CharField(max_length=20,null=True)
    phonenumber=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
    
    Hotel_id=models.ForeignKey(Hotel_Branches,on_delete=models.CASCADE)


class Manager(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=True)
    dateofbirth = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

    Hotel_id=models.ForeignKey(Hotel_Branches,on_delete=models.CASCADE)

class Rooms(models.Model):
    id =models.AutoField(primary_key=True)
    type =models.CharField(max_length=100,null=False)
    price =models.IntegerField(null=False)
    location =models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.type

    hotel_id=models.ForeignKey(Hotel_Branches,on_delete=models.CASCADE)


class Customers(models.Model):
    id =models.AutoField(primary_key=True)
    ssn =models.IntegerField(null=False)
    name =models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=True)
    phonenumber=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

    Hotel_id=models.ForeignKey(Hotel_Branches,on_delete=models.CASCADE)
    Room_id=models.ForeignKey(Rooms,on_delete=models.CASCADE)

    
class Dependents(models.Model):
    name =models.CharField(max_length=100,null=False)
    gender =models.CharField(max_length=100,null=False)
    dateofbirth = models.CharField(max_length=20,null=True)
    relationship = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
    Employee_id=models.ForeignKey(Employees,on_delete=models.CASCADE)

class Booking(models.Model):
    
    Bookingtype =models.CharField(max_length=100,null=False)
    
    Customer_id=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Room_id=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    Book_in=models.CharField(max_length=100,null=False)
    Book_out=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.Bookingtype