from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')

def about(request):
    return render(request,'dashboard/about.html')

def help(request):
    return render(request,'dashboard/help.html')

def tips(request):
    return render(request,'dashboard/tips.html')


