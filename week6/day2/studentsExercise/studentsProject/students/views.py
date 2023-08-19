from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@csrf_exempt
def student_list(request):
    if request.method == "GET":
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    if request.method == "POST":
        article_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=article_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)  # successfully created
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