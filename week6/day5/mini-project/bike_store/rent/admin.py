from django.contrib import admin
from .models import Rental, Vehicle, VehicleAtRentalStation, RentalStation, Address, Customer, RentalRate, VehicleSize, \
    VehicleType

# Register your models here.
admin.site.register(Rental)
admin.site.register(Vehicle)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(RentalRate)
admin.site.register(RentalStation)
admin.site.register(VehicleAtRentalStation)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)

