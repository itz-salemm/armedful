from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=50, null=True)
    subject = models.CharField(max_length=500, null=True)
    message = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name
        