from django.db import models
from datetime import timezone, date, datetime


# Create your models here.
class finalcopy(models.Model):
    Title = models.TextField(max_length=200, null=False)
    Project_Location = models.TextField(max_length=200, null=False)
    Proponent = models.TextField(max_length=200, null=False)
    Consultant = models.TextField(max_length=200, null=False)
    Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False)
    admin_upload = models.FileField(upload_to='media')


