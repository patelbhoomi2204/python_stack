from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    context = {
      'dateandtime': now
    }
    return render(request,'index.html', context)
