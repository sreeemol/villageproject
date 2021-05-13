import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Panchayath(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employees(models.Model):
    Panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "Employees")
    name = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name

class enduser(models.Model):
    Panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "enduser")
    name = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Leaveapplication(models.Model):
    panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "Leaveapplication")
    employees = models.ForeignKey(Employees,null = True,on_delete=models.CASCADE,related_name = "Employees")
    create_date = models.DateTimeField(default=timezone.now)
    leave_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=100)
    approved = models.BooleanField(default="False")
    def __str__(self):
        return self.employees

class Complaint(models.Model):
    panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "Complaint")
    enduser = models.ForeignKey(enduser,null = True,on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    
    description = models.CharField(max_length=100)
    solved = models.BooleanField(default="False")
    def __str__(self):
        return self.enduser

class News(models.Model):
    panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "News")
    create_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=100)
    
class Salary(models.Model):
    panchayath = models.ForeignKey(Panchayath,null = True,on_delete=models.CASCADE,related_name = "salary")
    employees = models.ForeignKey(Employees,null = True,on_delete=models.CASCADE,related_name = "salary")
    salary = models.IntegerField()
    ta = models.IntegerField()
    da = models.IntegerField()
    credited_on = models.DateTimeField(default=timezone.now)



