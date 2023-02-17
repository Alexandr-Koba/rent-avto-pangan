from django.db import models

class Project(models.Model):
    items = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=250)
    image = models.ImageField(upload_to='tehno/images/')
    url = models.URLField(blank=True)