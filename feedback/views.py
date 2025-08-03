from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics 
from .models import Employee  
from .serializers import Employeeserializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import Userregister
from .models import Feedback, Feedbackanswer
from .serializers import Feedbackserializer,Feedbackanswerserializer
from rest_framework.generics import ListAPIView 
from .serializers import Feedbackserializer,Feedbackquestionserializer ,Feedbackquestion
from rest_framework.permissions import IsAdminUser



# Create your views here.
class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    permission_classes = [IsAuthenticated]  
    


class Userregisterview(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userregister
class Submitfeedback(generics.CreateAPIView):
    serializer_class = Feedbackserializer
   
    def perform_create(self, serializer):
        employee = Employee.objects.get(user=self.request.user)
        serializer.save(employee=employee)
class FeedbackByEmployeeView(generics.ListAPIView):
    serializer_class = Feedbackserializer
    permission_classes = [IsAuthenticated] 
    def get_queryset(self):
            employee_id = self.kwargs['employee_id']
            return Feedback.objects.filter(employee__id=employee_id)
class Feedbackquestionview(generics.ListCreateAPIView):
    queryset = Feedbackquestion.objects.all()  
    serializer_class=Feedbackquestionserializer
    permission_classes=[IsAuthenticated]  

   
class Adminfeedbackfilter(ListAPIView):
    serializer_class=Feedbackserializer
    permission_classes=[IsAdminUser] 
    def get_queryset(self):
            queryset = Feedback.objects.all()
            designation=self.request.query_params.get('desigination') 
            department=self.request.query_params.get('department')     
            startdate=self.request.query_params.get('startdate')     
            enddate=self.request.query_params.get('enddate')         
        

            if designation:
                queryset = queryset.filter(employee__designation__name=designation)
            if department:
                queryset = queryset.filter(employee__department=department)
            if startdate and enddate:
                queryset = queryset.filter(created_at__range=[startdate, enddate])
    
            return queryset
            