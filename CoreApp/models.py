from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    address = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_per_meter = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name="member")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    area = models.DecimalField(max_digits=15, decimal_places=2)
    image_link = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.member} - {self.service} on {self.date_time}"
