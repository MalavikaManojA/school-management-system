from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', student_profile, name='student_profile'),
    # path('home/',student_home, name='student_home'),
    path('progress_card/', student_progress_card, name='student_progress_card')
    
]