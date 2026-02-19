from django.contrib import admin

from .models import Category, Room

admin.site.register(Category)
admin.site.register(Room)

from .models import Booking

from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'room', 'guests', 'arrival_date', 'departure_date')

