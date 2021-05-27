from django.db import models

# Create your models here.

class contact(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)

    def __str__(self):
        return self.fname