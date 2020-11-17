from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hashPW = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = hashPW, confirm_PW = hashPW)
        request.session['loggedInId'] = newUser.id
    return redirect("/success")

def success(request):
    if 'loggedInId' not in request.session:
        messages.error(request, "You must logged in first!")
        return redirect("/")
    context = {
        'loggedInUser': User.objects.get(id = request.session['loggedInId'])
    }
    return render(request, "success.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")

def login(request):
    print(request.POST)
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        userswithSameemail = User.objects.filter(email = request.POST['email'])
        request.session['loggedInId'] = userswithSameemail[0].id
    return redirect("/success")