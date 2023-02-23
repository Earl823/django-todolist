from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home.html', {})

def result(request):
    td = request.POST['todo']
    return render(request, 'result.html', {'name': td})

