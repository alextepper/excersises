"""
URL configuration for managementApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DepartmentAPIView, EmployeeAPIView, ProjectAPIView, TaskAPIView

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('departments/', DepartmentAPIView.as_view(), name='departments-list-create'),
    path('employees/', EmployeeAPIView.as_view(), name='employees-list-create'),
    path('projects/', ProjectAPIView.as_view(), name='projects-list'),
    path('projects/<int:pk>/', ProjectAPIView.as_view(), name='projects-detail'),
    path('tasks/', TaskAPIView.as_view(), name='tasks-list'),
    path('tasks/<int:pk>/', TaskAPIView.as_view(), name='tasks-detail'),
]

