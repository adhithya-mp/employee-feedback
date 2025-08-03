from django.contrib import admin
from .models import Designation,Employee,Feedback,Feedbackquestion,Feedbackanswer


# Register your models here.
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Feedback)
admin.site.register(Feedbackquestion)
admin.site.register(Feedbackanswer)
