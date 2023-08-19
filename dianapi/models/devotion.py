from django.db import models

class Devotion(models.Model):
  date = models.DateField()
  verse = models.CharField(max_length=10000)
  content = models.CharField(max_length=10000)
