from django.shortcuts import render
from api import serializers
from api import models
from rest_framework.response import Response
from rest_framework import viewsets



class InstructorAPI(viewsets.ModelViewSet):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer

class CourseAPI(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer