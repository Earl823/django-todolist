from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

# this ia the hompage function
def index(request):
    td = request.POST['todo']
    insert = Item(text=td, complete=False)
    #btn = request.POST['remove']


    item = Item.objects.all()
    #Item.objects.filter(id=btn).delete()

    insert.save()
    
    return render(request, 'home.html', {'name': item})



