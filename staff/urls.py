from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',staff_profile, name='staff_profile'),
    path('signup/', student_signup,name='student_signup'),
    path('student/list/', student_list, name='student_list'),
    path('student/detail/<int:id>/', student_detail, name='student_detail'),
    path('student/update/<int:id>/',update_student_detail, name='student_update'),
    path('home/',staff_home, name='staff_home'),
    path('mark/<int:id>/', student_mark_form, name='student_mark_form'),
    path('marklist/<int:s_id>/<int:term>/', student_marklist, name='student_marklist'),
    path('send/card/<int:t_id>/',send_progress_card,name='send_progress_card'),
    path('card/<int:s_id>/',progress_card,name='progress_card'),
]