from django.db import models

# Create your models here.

class Upload(models.Model):
    profile=models.FileField(upload_to='static/fileUpload')
    doc=models.FileField(upload_to='static/fileUpload')
