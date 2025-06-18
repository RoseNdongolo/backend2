from django.contrib import admin
from .models import Airline, Flight, Booking,Passenger, Payment, Seat

admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Passenger)
admin.site.register(Payment)
admin.site.register(Seat)