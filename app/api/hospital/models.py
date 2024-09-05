from django.db import models
# from api.bed import models as m

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

    class Meta:
        # Optional: Customizing the plural form and ordering
        verbose_name_plural = "Hospitals"
        ordering = ['-created_at']
