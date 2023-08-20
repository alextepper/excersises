from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course, related_name='teachers')

    def __str__(self):
        return self.name


class SchoolFacility(models.Model):
    facility_name = models.CharField(max_length=200)
    usage_purpose = models.TextField()

    def __str__(self):
        return self.facility_name

class Laboratory(SchoolFacility):
    equipment_list = models.TextField()

    class Meta:
        verbose_name_plural = "Laboratories"