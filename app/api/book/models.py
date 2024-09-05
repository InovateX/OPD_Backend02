from django.db import models
from api.doctor.models import Doctor

class Book(models.Model):
    # Define the fields for the Book model
    date = models.DateField()  # Field for the date
    time = models.TimeField()  # Field for the time
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Field for the price

    # ForeignKey field to reference the Doctor model
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='books')

    # Timestamps for creation and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking with Dr. {self.doctor.name} on {self.date} at {self.time}"

    class Meta:
        verbose_name_plural = "Books"
        ordering = ['-date', '-time']

# Create your models here.
