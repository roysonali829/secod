from django.urls import path
from app2.views import*
app_name='nothing'

urlpatterns =[
    path('second/',second,name='second'),
    path('new3/',new3,name='new3.html'),
    path('new4/',new4,name='new4.html'),
]