from django.urls import path
from app1.views import *
app_name='somthing'


urlpatterns=[
    path('first/',first,name='first'),
    path('new1/',new1,name='new1.html'),
    path('new2/',new2,name='new2.html'),
]