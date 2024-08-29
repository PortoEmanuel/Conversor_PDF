from django.db import models

class Arquivo(models.Model):
    arquivo = models.FileField(upload_to='uploads/')
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
