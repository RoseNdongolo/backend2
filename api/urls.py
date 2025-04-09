from django.urls import path, include
from rest_framework.routers import DefaultRouter
from flight.views import *
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'airlines',AirlineViewSet   ,basename='airline')
router.register(r'flights', FlightViewSet ,basename='flight')
router.register(r'bookings', BookingViewSet    ,basename='booking')
router.register(r'payments', PaymentViewSet  ,basename='payment')
router.register(r'seats',SeatViewSet    ,basename='seat')

urlpatterns = [
    path('', include(router.urls)),  
    path('login/', obtain_auth_token, name='api_token_auth'),

]


