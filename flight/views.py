# # flight/views.py

from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]


class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ModelViewSet):
    queryset=Seat.objects.all()
    serializer_class=SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# from rest_framework import viewsets
# from .models import Airline
# from .serializers import AirlineSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class AirlineViewSet(viewsets.ModelViewSet):
#     queryset = Airline.objects.all()
#     serializer_class = AirlineSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
