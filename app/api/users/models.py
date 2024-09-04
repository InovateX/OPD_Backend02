from django.db import models  
from django.core.validators import MinLengthValidator, RegexValidator  
from django.contrib.auth.password_validation import validate_password  
  
class UserModel(models.Model):  
   name = models.CharField(max_length=255)  
   email = models.EmailField()  
   phone_no = models.CharField(max_length=10)  
   password = models.CharField(max_length=255, validators=[  
      MinLengthValidator(8),  
      RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_$])[A-Za-z\d@_$]{8,}$',  
                'Password must contain at least one lowercase letter, one uppercase letter, one digit, and one special character (@, _, or $).'),  
      validate_password,  # Use Django's built-in password validation  
   ])  
   identification_type = models.CharField(max_length=20, choices=[  
      ('AADHAR', 'Aadhar'),  
      ('PAN', 'PAN'),  
      ('PASSPORT', 'Passport'),  
      ('DRIVING_LICENSE', 'Driving License'),  
   ])  
   id_no = models.CharField(max_length=50)  
   age = models.IntegerField()  
   location = models.CharField(max_length=255)  
   state = models.CharField(max_length=100)  
   city = models.CharField(max_length=100)  
   pin_code = models.CharField(max_length=10)  # Increased max length to 10  
  
   created_at = models.DateTimeField(auto_now_add=True)  
   updated_at = models.DateTimeField(auto_now=True)  
  
   def __str__(self):  
      return self.name  
  
   class Meta:  
      verbose_name_plural = "User Models"  
      ordering = ['-created_at']


