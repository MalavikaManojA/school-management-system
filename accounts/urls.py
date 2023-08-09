from django.urls import path
from .views import *

urlpatterns = [
    path('signin/',signin,name='signin'),
    path('about/', about_page,name='about'),
    path('contact/', contact_page,name='contact'),
    path('logout/',action_logout, name='logout'),
    path('change_password/',change_password,name='change_password')
]