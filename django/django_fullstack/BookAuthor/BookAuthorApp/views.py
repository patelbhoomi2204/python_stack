from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'allBooks' : Book.objects.all()
    }
    return render(request, "index.html", context)

def addBook(request):
    print(request.POST)
    Book.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    return redirect("/")

def showBook(request, idBook):
    context = {
        'oneBook': Book.objects.get(id=idBook),
        'authors': Author.objects.all
    }
    return render(request, "bookInfo.html", context)

def bookAuthor(request, idBook):
    this_book= Book.objects.get(id=idBook)
    this_author= Author.objects.get(id=request.POST['Author'])
    this_book.writer.add(this_author)
    return redirect(f"/books/{idBook}")