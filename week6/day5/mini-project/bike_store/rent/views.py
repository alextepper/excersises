# views.py
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils.datetime_safe import date, datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rental, Vehicle, Customer, VehicleType, RentalStation, VehicleAtRentalStation
from .serializers import RentalSerializer, CustomerSerializer, VehicleSerializer, VehicleTypeWithVehiclesSerializer, \
    RentalStationSerializer, DetailedRentalStationSerializer, StationDistributionSerializer


class RentalListView(APIView):

    def get(self, request):
        # Query all rentals, unreturned first, then ordered by date ascending
        rentals = Rental.objects.filter(return_date__isnull=True).union(
            Rental.objects.filter(return_date__isnull=False),
            all=True
        ).order_by('rental_date')

        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            # Checking if the vehicle is currently rented
            if Rental.objects.filter(vehicle=serializer.validated_data['vehicle'], return_date__isnull=True).exists():
                return Response({'error': 'Vehicle is currently rented.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalDetailView(APIView):

    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            return None

    def get(self, request, pk):
        rental = self.get_object(pk)
        if rental:
            serializer = RentalSerializer(rental)
            return Response(serializer.data)
        return Response({'error': 'Rental not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        rental = self.get_object(pk)
        if rental:
            serializer = RentalSerializer(rental, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Rental not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        rental = self.get_object(pk)
        if rental:
            rental.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Rental not found'}, status=status.HTTP_404_NOT_FOUND)


class CustomerListView(APIView):

    def get(self, request):
        # Query all customers in alphabetical order by last name and then by first name
        customers = Customer.objects.order_by('last_name', 'first_name')

        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomerAddView(APIView):

    def get(self, request):
        serializer = CustomerSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleListView(APIView):

    def get(self, request):
        vehicle_types = VehicleType.objects.prefetch_related('vehicle_set').all()
        serializer = VehicleTypeWithVehiclesSerializer(vehicle_types, many=True)
        return Response(serializer.data)


class VehicleDetailView(APIView):

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return None

    def get(self, request, pk):
        vehicle = self.get_object(pk)
        if vehicle:
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        vehicle = self.get_object(pk)
        if vehicle:
            serializer = VehicleSerializer(vehicle, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        vehicle = self.get_object(pk)
        if vehicle:
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)


class VehicleAddView(APIView):

    def get(self, request):
        serializer = VehicleSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalStationListView(APIView):

    def get(self, request):
        rental_stations = RentalStation.objects.all()
        serializer = RentalStationSerializer(rental_stations, many=True)
        return Response(serializer.data)


class RentalStationAddView(APIView):

    def get(self, request):
        serializer = RentalStationSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalStationDetailView(APIView):

    def get(self, request, station_id):
        try:
            station = RentalStation.objects.get(pk=station_id)
        except RentalStation.DoesNotExist:
            return Response({"error": "Rental station not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetailedRentalStationSerializer(station)
        return Response(serializer.data)


class StationDistributionView(APIView):

    def get(self, request):
        stations = RentalStation.objects.all()
        serializer = StationDistributionSerializer(stations, many=True)
        return Response(serializer.data)


class StationDistributeView(APIView):

    def post(self, request):
        stations = RentalStation.objects.all()
        vehicles = VehicleAtRentalStation.objects.filter(departure_date__isnull=True)

        if not stations or not vehicles:
            return Response({"error": "No stations or vehicles available for distribution."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Distribute vehicles evenly among stations
        vehicles_per_station = len(vehicles) // len(stations)

        for station in stations:
            # Get vehicles already at the station
            current_vehicle_count = station.vehicleatrentalstation_set.filter(departure_date__isnull=True).count()
            # Calculate the number of vehicles to move to the station
            vehicles_to_move = vehicles_per_station - current_vehicle_count
            # Move vehicles to the station
            for _ in range(vehicles_to_move):
                if vehicles:
                    vehicle_to_move = vehicles.pop()
                    vehicle_to_move.departure_date = None  # Reset departure date
                    vehicle_to_move.save()

        return Response({"message": "Vehicles distributed among stations successfully."}, status=status.HTTP_200_OK)


class AddVehicleToStationView(APIView):

    def post(self, request, vehicle_id, station_id):
        try:
            station = RentalStation.objects.get(pk=station_id)
        except RentalStation.DoesNotExist:
            return Response({"error": "Station not found."}, status=status.HTTP_404_NOT_FOUND)

        vehicle_at_station = VehicleAtRentalStation(
            arrival_date=date.today(),
            vehicle_id=vehicle_id,
            station=station
        )
        vehicle_at_station.save()

        return Response({"message": "Vehicle added to the station successfully."}, status=status.HTTP_201_CREATED)


class RemoveVehicleFromStationView(APIView):

    def post(self, request, vehicle_id, station_id):
        try:
            vehicle_at_station = VehicleAtRentalStation.objects.get(vehicle_id=vehicle_id, station_id=station_id, departure_date__isnull=True)
        except VehicleAtRentalStation.DoesNotExist:
            return Response({"error": "Vehicle not currently at the specified station."}, status=status.HTTP_404_NOT_FOUND)

        vehicle_at_station.departure_date = date.today()
        vehicle_at_station.save()

        return Response({"message": "Vehicle removed from the station successfully."}, status=status.HTTP_200_OK)


class VehiclesAtStationView(APIView):

    def get(self, request, station_id):
        vehicles = VehicleAtRentalStation.objects.filter(station_id=station_id, departure_date__isnull=True)
        data = [{"vehicle_id": vehicle.vehicle_id, "arrival_date": vehicle.arrival_date} for vehicle in vehicles]
        return Response(data, status=status.HTTP_200_OK)


class MonthlyRentalStats(APIView):

    def get(self, request):
        # Grouping by month
        stats = (Rental.objects
                 .annotate(month=TruncMonth('rental_date'))
                 .values('month')
                 .annotate(rental_count=Count('id'))
                 .order_by('month'))

        # Transforming queryset to desired output format
        data = {item['month'].strftime('%Y-%m'): item['rental_count'] for item in stats}

        return Response(data)


class PopularRentalStation(APIView):

    def get(self, request):
        # Counting rentals per station and ordering by count in descending order
        stats = (Rental.objects
                 .values('station__name')  # use the name of the associated station
                 .annotate(rental_count=Count('id'))
                 .order_by('-rental_count'))

        # Transforming queryset to desired output format
        data = {item['station__name']: item['rental_count'] for item in stats}

        return Response(data)


class PopularVehicleTypeView(APIView):
    def get(self, request, *args, **kwargs):
        counts = (
            Rental.objects.values('vehicle__vehicle_type__name')
            .annotate(total_rented=Count('vehicle__vehicle_type'))
            .order_by('-total_rented')
        )
        data = {item['vehicle__vehicle_type__name']: item['total_rented'] for item in counts}
        return Response(data, status=status.HTTP_200_OK)


class PopularVehicleTypeView(APIView):
    def get(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        rentals = Rental.objects.all()

        if start_date and end_date:
            try:
                formatted_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                formatted_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
                rentals = rentals.filter(rental_date__range=(formatted_start_date, formatted_end_date))
            except ValueError:
                return Response({"error": "Invalid date format. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

        counts = (
            rentals.values('vehicle__vehicle_type__name')
            .annotate(total_rented=Count('vehicle__vehicle_type'))
            .order_by('-total_rented')
        )

        data = {item['vehicle__vehicle_type__name']: item['total_rented'] for item in counts}
        return Response(data, status=status.HTTP_200_OK)
