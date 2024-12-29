from django.db import models
from django.utils.timezone import now

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Developer', 'Developer'),
        ('Manager', 'Manager'),
        ('HR', 'HR'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    courses = models.CharField(max_length=255)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
