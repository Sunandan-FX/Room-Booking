from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length= 200)
    email = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 200)
    room_number = models.IntegerField()
    booked_date = models.DateTimeField(auto_now_add=True)
    feedback = models.CharField(max_length=1000)

