from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Designation(models.Model):
    designation=models.CharField(max_length=100)
 
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=100)
    pincode=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    designation=models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True)
 



class Feedback(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='feedback')     
    rating=models.IntegerField(choices=[(i,i)for i in range(1,6)])
    comment=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now_add=True)

class Feedbackquestion(models.Model) :
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('rating', 'Rating'),)
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text
class Feedbackanswer(models.Model):
    feedback=models.ForeignKey(Feedback,on_delete=models.CASCADE,related_name='answers')
    question=models.ForeignKey(Feedbackquestion,on_delete=models.CASCADE)
   
    text_answer = models.TextField(max_length=5000, blank=True, null=True)
    rating_answer = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)
    
