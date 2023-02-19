from django.db import models

class Blog(models.Model):
    items = models.CharField(max_length=200)
    descriptions = models.TextField()
    date = models.DateField()