from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guests = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - Room {self.room} - {self.guests} Guests"
