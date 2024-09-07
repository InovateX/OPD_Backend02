from django.db import models

class Opd(models.Model):
   #doctor = models.CharField(max_length=255) 
   type = models.CharField(max_length=50, choices=[  
      ('GENERAL', 'General OPD'),  
      ('SPECIALTY', 'Specialty OPD'),  
      ('EMERGENCY', 'Emergency OPD'),  
      ('CARDIOLOGY', 'Cardiology OPD'),  
      ('NEUROLOGY', 'Neurology OPD'),  
      ('ONCOLOGY', 'Oncology OPD'),
      ('GYNAECOLOGY', 'Gynaecology OPD'),   
   ])     
   time = models.TimeField()  
   date = models.DateField()  
   off = models.BooleanField(default=False)  # Assuming 'off' means whether the OPD is closed   
  
   # Fields to store the creation and last modification timestamps  
   created_at = models.DateTimeField(auto_now_add=True)  
   updated_at = models.DateTimeField(auto_now=True)

  
  
   def __str__(self):  
      return f"Opd on {self.date} at {self.time} - Doctor: {self.doctors}"  
  
   class Meta: 
      verbose_name = "Opd"  
      verbose_name_plural = "Opds"  
      ordering = ['-date', '-time']
      

