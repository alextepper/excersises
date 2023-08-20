import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Customer, Address, RentalStation, Rental, Vehicle, VehicleType, VehicleSize
from faker import Faker
import random

fake = Faker()


def create_customers(number):
    for _ in range(number):
        address = Address(
            address=fake.street_address(),
            address2=fake.secondary_address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.zipcode()
        )
        address.save()

        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=address
        )
        customer.save()

    print(f"CREATED {number} Customers")


def create_stations(number):
    for _ in range(number):
        address = Address(
            address=fake.street_address(),
            address2=fake.secondary_address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.zipcode()
        )
        address.save()

        station = RentalStation(
            name=address.address,
            capacity = 200,
            address = address
        )
        station.save()

    print(f"CREATED {number} Stations")


def create_rentals(number):
    customers = list(Customer.objects.all())
    vehicles = list(Vehicle.objects.all())
    stations = list(RentalStation.objects.all())

    if not customers or not vehicles or not stations:
        print("Ensure that there are enough Customers, Vehicles, and Rental Stations in the database.")
        return

    for _ in range(number):
        rental = Rental(
            rental_date=fake.date_this_decade(),
            return_date=fake.date_this_decade() if fake.boolean(chance_of_getting_true=70) else None,  # 70% chance the vehicle was returned
            customer=random.choice(customers),
            vehicle=random.choice(vehicles),
            station=random.choice(stations)  # assuming Rental model has a ForeignKey to RentalStation
        )
        rental.save()

    print(f"CREATED {number} Rentals")


def create_vehicles(number):
    vehicle_types = list(VehicleType.objects.all())
    vehicle_sizes = list(VehicleSize.objects.all())

    if not vehicle_types or not vehicle_sizes:
        print("Ensure that there are enough Vehicle Types and Vehicle Sizes in the database.")
        return

    for _ in range(number):
        vehicle = Vehicle(
            vehicle_type=random.choice(vehicle_types),
            date_created=fake.date_this_decade(),
            real_cost=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            size=random.choice(vehicle_sizes)
        )
        vehicle.save()

    print(f"CREATED {number} Vehicles")


create_rentals(2000)
