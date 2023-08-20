# serializers.py

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Rental, Customer, VehicleType, Vehicle, RentalStation, VehicleAtRentalStation


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleTypeWithVehiclesSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)

    class Meta:
        model = VehicleType
        fields = ('name', 'vehicles')


class RentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalStation
        fields = '__all__'


class VehicleAtStationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleAtRentalStation
        fields = ('vehicle', 'arrival_date', 'departure_date')


class DetailedRentalStationSerializer(serializers.ModelSerializer):
    vehicles_at_station = VehicleAtStationSerializer(source='vehicleatrentalstation_set', many=True)

    class Meta:
        model = RentalStation
        fields = ('name', 'capacity', 'address', 'vehicles_at_station')


class StationDistributionSerializer(serializers.ModelSerializer):
    vehicle_count = serializers.SerializerMethodField()

    class Meta:
        model = RentalStation
        fields = ('name', 'vehicle_count', 'capacity')

    def get_vehicle_count(self, obj):
        return obj.vehicleatrentalstation_set.filter(departure_date__isnull=True).count()
