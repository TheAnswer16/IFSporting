from django.shortcuts import render
from . models import *

# Create your views here.
def login(request):
    
    return render(request, 'auth/login.html')