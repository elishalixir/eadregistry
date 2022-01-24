from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import timezone, date, datetime


# Create your models here.
class finalcopy(models.Model):
    Title = models.TextField(max_length=200, null=False)
    Sector = models.TextField(max_length=50, null=True)
    Project_Location = models.TextField(max_length=200, null=False)
    Project_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    Proponent = models.TextField(max_length=200, null=False)
    Consultant = models.TextField(max_length=200, null=False)
    Division = models.TextField(max_length=50, null=False)
    Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False)
    pdf_upload = models.FileField(upload_to='media', max_length=150,
                                  validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return self.Title + " | " + self.Proponent


