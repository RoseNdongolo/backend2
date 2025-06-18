from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    PASSENGER = 'passenger', _('Passenger')


# custom user model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
    )
    
    def __str__(self):
        return self.username    


# airline model
class Airline(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

# flight model
class Flight(models.Model):
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE, related_name='flight_from_airline')
    flight_number = models.CharField(max_length=10, unique=True)
    destination = models.ForeignKey('Airline', on_delete=models.CASCADE, related_name='flight_to_destination')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seat_available = models.PositiveBigIntegerField()

    def __str__(self):
        return self.flight_number


# passenger model
class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger_profile', limit_choices_to={'role': Roles.PASSENGER})
    passport_number = models.CharField(max_length=20, unique=True)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
    ])

    def __str__(self):
        return self.user.username


# booking model
class Booking(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='booking')
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_status_choices = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending')
    ]
    booking_status = models.CharField(max_length=10, choices=booking_status_choices, default='pending')

    def __str__(self):
        return self.booking_status


# payment model
class Payment(models.Model):
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status_choice = [
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('pending', 'Pending')
    ]
    payment_status = models.CharField(max_length=10, choices=payment_status_choice, default='pending')

    def __str__(self):
        return self.payment_status


# seat model
class Seat(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='seat')
    seat_number = models.CharField(max_length=5)
    is_booking = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number
