from django.urls import path
from .views import EmployeeView, Userregisterview, Submitfeedback,FeedbackByEmployeeView,Feedbackquestionview,Adminfeedbackfilter

from django.http import JsonResponse

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='employee-list-create'),
    path('register/', Userregisterview.as_view(), name='user-register'),
    path('submit/', Submitfeedback.as_view(), name='submit-feedback'),
    path('feedback/<int:employee_id>/', FeedbackByEmployeeView.as_view(), name='feedback-by-employee'),
    path('question/', Feedbackquestionview.as_view(), name='feedback-question'),
    path('admin-feedback/',Adminfeedbackfilter.as_view(),name='admin-feedback'),

    path('',lambda request:JsonResponse({'message':'welcome to employee feedback app'})),
]
