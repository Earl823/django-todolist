from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import UserItem
# Create your views here.

# this ia the hompage function
def index(request):
    #td = request.POST['todo']
    #insert = Item(text=td, complete=False)
    #btn = request.POST['remove']


    #item = Item.objects.all()
    #Item.objects.filter(id=btn).delete()

    #insert.save()
    form = UserItem()
    context = {'form': form}
    return render(request, 'home.html', context)



