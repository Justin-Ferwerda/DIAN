from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mailer_lite_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name
