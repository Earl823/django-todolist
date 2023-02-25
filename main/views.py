from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# this ia the hompage function
def index(request):
    td = request.POST['todo']
    return render(request, 'home.html', {'name': td})



