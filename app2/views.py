from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second(request):
    return HttpResponse('<h1>heyyyyyyyy</h1>')
def new3(request):
    return render(request,'new3.html')
def new4(request):
    return render(request,'new4.html')


    