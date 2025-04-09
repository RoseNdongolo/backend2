from django.db import models

# Airline Model
class Airline(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    Logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Name
    

# Flight Model
class Flight(models.Model):
    Airline = models.ForeignKey('Airline', on_delete=models.CASCADE, related_name='Flight_from_Airline')
    Flight_number = models.CharField(max_length=10, unique=True)
    Destination = models.ForeignKey('Airline', on_delete=models.CASCADE, related_name='Flight_to_destination')
    Departure_time = models.DateTimeField()
    Arrival_time = models.DateTimeField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Seat_available = models.PositiveBigIntegerField()

    def __str__(self):
        return self.Flight_number


# Booking Model
class Booking(models.Model):
    Flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='Booking')
    Booking_date = models.DateTimeField(auto_now_add=True)
    BOOKING_STATUS_CHOICES = [
        ('CONFIRMED', 'confirmed'),
        ('CANCELLED', 'cancelled'),
        ('PENDING', 'pending')
    ]
    Booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.Booking_status


# Payment Model
class Payment(models.Model):
    Booking = models.ForeignKey('Booking', on_delete=models.CASCADE, related_name='Payment')
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_date = models.DateTimeField(auto_now_add=True)
    PAYMENT_STATUS_CHOICE = [
        ('PAID', 'paid'),
        ('FAILED', 'failed'),
        ('PENDING', 'pending')
    ]
    Payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICE, default='PENDING')

    def __str__(self):
        return self.Payment_status


# Seat Model
class Seat(models.Model):
    Flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='Seat')
    Seat_number = models.CharField(max_length=5)
    Is_booking = models.BooleanField(default=False)

    def __str__(self):
        return self.Seat_number
