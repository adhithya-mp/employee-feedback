from rest_framework import serializers
from .models import Designation,Employee,Feedback,Feedbackquestion,Feedbackanswer
from django.contrib.auth.models import User

class Designationserializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'
class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'    
class Feedbackanswerserializer(serializers.ModelSerializer):
    text_answer = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    rating_answer = serializers.IntegerField(required=False, allow_null=True)
    class Meta:

        model=Feedbackanswer 
        fields = ['question', 'text_answer', 'rating_answer']          
class Feedbackserializer(serializers.ModelSerializer):
    answers = Feedbackanswerserializer(many=True)
    class Meta:
        model=Feedback
        fields=['employee', 'rating', 'comment', 'date', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        feedback = Feedback.objects.create(**validated_data)

        for answer_data in answers_data:
            Feedbackanswer.objects.create(feedback=feedback, **answer_data)

        return feedback

class Feedbackquestionserializer(serializers.ModelSerializer):
   
    class Meta:
        model=Feedbackquestion
        fields='__all__'
       



        
class Userregister(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User     
        fields=['username','email','password']   
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],      
            password=validated_data['password']
        )
        return user                         
