from django.db import models
from api.hospital.models import Hospital

class Admission(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()
    referred_by = models.TextField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='admissions')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Admission of {self.name} at {self.hospital.name}"

    class Meta:
        verbose_name_plural = "Admissions"
        ordering = ['-created_at']

# Create your models here.
