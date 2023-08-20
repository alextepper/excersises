# urls.py

from django.urls import path
from .views import RentalListView, RentalDetailView, CustomerListView, CustomerAddView, VehicleDetailView, \
    VehicleAddView, RentalStationListView, RentalStationAddView, RentalStationDetailView, StationDistributionView, \
    StationDistributeView, VehicleListView, AddVehicleToStationView, RemoveVehicleFromStationView, \
    VehiclesAtStationView, MonthlyRentalStats, PopularRentalStation, PopularVehicleTypeView

urlpatterns = [
    path('rental/', RentalListView.as_view(), name='rental-list'),
    path('rental/<int:pk>/', RentalDetailView.as_view(), name='rental-detail'),
    path('customer/', CustomerListView.as_view(), name='customer-list'),
    path('customer/add', CustomerAddView.as_view(), name='customer-add'),
    path('vehicle/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicle/add', VehicleAddView.as_view(), name='vehicle-add'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('station/', RentalStationListView.as_view(), name='rental-station-list'),
    path('station/add', RentalStationAddView.as_view(), name='rental-station-add'),
    path('station/<int:station_id>/', RentalStationDetailView.as_view(), name='rental-station-detail'),
    path('station/distribution', StationDistributionView.as_view(), name='station-distribution'),
    path('station/distribute', StationDistributeView.as_view(), name='station-distribute'),
    path('station/<int:station_id>/add_vehicle/<int:vehicle_id>/', AddVehicleToStationView.as_view(), name='add-vehicle-to-station'),
    path('station/<int:station_id>/remove_vehicle/<int:vehicle_id>/', RemoveVehicleFromStationView.as_view(), name='remove-vehicle-from-station'),
    path('station/<int:station_id>/vehicles/', VehiclesAtStationView.as_view(), name='vehicles-at-station'),
    path('stats/monthly', MonthlyRentalStats.as_view(), name='monthly-rental-stats'),
    path('stats/popular_station', PopularRentalStation.as_view(), name='popular-rental-station'),
    path('rent/stats/popular_vehicle_type', PopularVehicleTypeView.as_view(), name='popular-vehicle-type'),



]

