from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('api/teachers/', views.TeacherList.as_view(), name='teacher_list'),
    path('api/facilities/', views.AllSchoolFacilities.as_view(), name='all_facilities'),
    path('api/laboratories/', views.AllLaboratories.as_view(), name='all_laboratories'),

]
