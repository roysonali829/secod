from django.urls import path
from app3.views import *
app_name='anything'

urlpatterns = [
    path('third/',third,name='third'),
    path('new5/',new5,name='new5.html'),
    path('new6/',new6,name='new6.html'),
]