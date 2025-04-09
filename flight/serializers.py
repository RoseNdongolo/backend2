from rest_framework import serializers
from .models import *

# flight/serializers.py

from rest_framework import serializers
from .models import Airline

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'  


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'  

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__' 


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields='__all__'