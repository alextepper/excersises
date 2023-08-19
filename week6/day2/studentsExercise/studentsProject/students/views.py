import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer


class StudentView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
def student_list(request):
    if request.method == 'GET':

        date_joined = request.GET.get('date_joined')

        if date_joined:
            students = Student.objects.filter(date_joined__date=date_joined)
        else:
            students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def student_detail(request, student_pk):
    try:
        student = Student.objects.get(pk=student_pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404) # Not found

    if request.method == 'GET':
       serializer = StudentSerializer(student)
       return JsonResponse(data=serializer.data)
    elif request.method == 'PUT':
        new_student = JSONParser(request)
        serializer = StudentSerializer(student, data=new_student)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)
    elif request.method == 'DELETE':
       student.delete()
       return HttpResponse(status=204) # Successfully deleted