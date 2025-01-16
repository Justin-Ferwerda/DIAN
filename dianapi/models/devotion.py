from django.db import models

class Devotion(models.Model):
    date = models.DateField()
    verse = models.TextField()
    content = models.TextField()
    
    def __str__(self):
        return str(self.date.strftime('%b. %-d'))
    
