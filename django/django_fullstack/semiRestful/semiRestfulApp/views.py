from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def newShow(request):
    return render(request, "index.html")

def shows(request):
    print(Show.objects.all())
    context = {
        'allShows' : Show.objects.all()
    }
    return render(request, "shows.html", context)

def createShow(request):
    errorFromValidator = Show.objects.createShowValidator(request.POST)
    if len(errorFromValidator)>0:
        for key, value in errorFromValidator.items():
            messages.error(request, value)
        return redirect('/shows/new')
    newShow = Show.objects.create(name=request.POST['title'], network=request.POST['network'], release_date=request.POST['rel'], Description=request.POST['desc'])
    return redirect(f"/shows/{newShow.id}")

def showInfo(request, showId):
    context = {
        'oneShow': Show.objects.get(id=showId)
    }
    return render(request, "showInfo.html", context)

def editShow (request, showId):
    context = {
        'showDetails': Show.objects.get(id=showId)
    }
    return render(request, "editShows.html", context)

def updateShow(request, showId):
    show = Show.objects.get(id=showId)
    show.name=request.POST['title']
    show.network=request.POST['network']
    show.release_date=request.POST['rel']
    show.Description=request.POST['desc']
    show.save()
    return redirect(f"/shows/{showId}")


def deleteShow(request, showId):
    print(showId)
    showTodelete = Show.objects.get(id=showId)
    showTodelete.delete()
    return redirect("/shows")