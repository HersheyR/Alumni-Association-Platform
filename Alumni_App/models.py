from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    graduation_year = models.IntegerField()
    degree = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)  # New field

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
