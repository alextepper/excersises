from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import SchoolFacilitySerializer, LaboratorySerializer, TeacherSerializer


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})


class TeacherList(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class AllSchoolFacilities(APIView):
    def get(self, request):
        facilities = SchoolFacility.objects.all()
        serializer = SchoolFacilitySerializer(facilities, many=True)
        return Response(serializer.data)


class AllLaboratories(APIView):
    def get(self, request):
        labs = Laboratory.objects.all()
        serializer = LaboratorySerializer(labs, many=True)
        return Response(serializer.data)