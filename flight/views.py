# # # flight/views.py

# from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

# from rest_framework.permissions import IsAuthenticatedOrReadOnly



class AirlineViewSet(viewsets.ModelViewSet):  # ✅ use viewsets.ModelViewSet
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer  
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer 
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnl

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]



class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class SeatViewSet(viewsets.ModelViewSet):
    queryset=Seat.objects.all()
    serializer_class=SeatSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly]



from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
