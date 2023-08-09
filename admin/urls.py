from django.urls import path
from .views import *

urlpatterns = [
    path('staff/list/',admin_page,name='admin_page'),
    path('staff/signup/', staff_signup, name='admin_staff_signup'),
    path('staff/detail/<int:id>/',staff_in_detail, name='staff_in_detail'),
    path('staff/update/<int:id>',update_staff_detail, name='update_staff_detail'),
    path('subject/',add_subject,name='add_subject'),
    path('student_list/<int:a_id>/',teacher_student_list,name='teacher_student_list')
   
]