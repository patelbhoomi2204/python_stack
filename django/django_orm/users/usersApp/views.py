from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'allUsers' : User.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    print(request.POST)
    User.objects.create(first_name = request.POST['fname'],last_name = request.POST['lname'],email_address = request.POST['email'], age = request.POST['age'])
    return redirect('/')

