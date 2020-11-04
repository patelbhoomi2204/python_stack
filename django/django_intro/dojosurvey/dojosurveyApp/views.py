from django.shortcuts import render, HttpResponse, redirect
def index(request):
    print(request.method)
    return render(request, "form.html")

def formInfo(request):
    print(request.method)
    print(request.POST)
    print(request.POST['name'])
    request.session['forminfo'] = request.POST
    return redirect('/success')

def showResults(request):
    print('request.post in the showResults function', request.POST)
    context = {
      'formDetails' : request.POST
    }
    return render(request, "result.html")
