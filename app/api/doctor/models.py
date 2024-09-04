from django.db import models
from api.opd.models import Opd
from django.apps import apps


class Doctor(models.Model):  
   name = models.CharField(max_length=255)  # Name of the doctor  
   email = models.EmailField()  # Email address of the doctor  
   contact = models.CharField(max_length=20, blank=True, null=True)  # Contact number of the doctor (optional)  
   designation = models.CharField(max_length=100)  # Designation of the doctor  
  
   # Fields to store the creation and last modification timestamps  
   created_at = models.DateTimeField(auto_now_add=True)  
   updated_at = models.DateTimeField(auto_now=True)

   
   opd = models.ForeignKey(Opd, on_delete=models.CASCADE, related_name='doctors')


   def __str__(self):  
      return self.name  
  
   class Meta:  
      # Optional: Customizing the plural form and ordering  
      verbose_name_plural = "Doctors"  
      ordering = ['-created_at']
