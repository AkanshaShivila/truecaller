from django.db import models

class Person(models.Model):
    phone_no = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_no
