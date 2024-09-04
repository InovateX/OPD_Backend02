from django.db import models
from api.hospital.models import Hospital

class Bed(models.Model):
    WARD_CHOICES = [
        ('ICU', 'Intensive Care Unit'),
        ('GW', 'General Ward'),
        ('A&E', 'Accident and Emergency Ward'),
        ('CCU', 'Cardiac Care Unit'),
        ('PICU', 'Pediatric Intensive Care Unit'),
        ('NICU', 'Neonatal Intensive Care Unit'),
        ('HDU', 'High Dependency Unit'),
        ('MSW', 'Medical and Surgical Ward'),
        ('ONCOLOGY', 'Oncology'),
    ]

    ward_type = models.CharField(max_length=255, choices=WARD_CHOICES)
    capacity = models.IntegerField()
    occupied = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='beds')

    def __str__(self):
        return f"{self.ward_type} - {self.hospital.name}"

    class Meta:
        verbose_name_plural = "Beds"
        ordering = ['-created_at']
