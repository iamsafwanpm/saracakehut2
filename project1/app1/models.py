from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
class Consultation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField() 
    time = models.TimeField()

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Register(models.Model):
    Name=models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    # Add the 'name' field
    name = models.CharField(max_length=100)

    # Other fields for the booking model
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # Add other fields as needed, such as date, time, customer information, etc.
    
    def __str__(self):
        return self.name