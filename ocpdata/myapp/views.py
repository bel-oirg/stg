from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

people = [
	{'id':1, 'name' : 'buddha'},
	{'id':2, 'name' : 'li 7wak'} 
]

def home_page(request):
	people = Room.objects.all()
	return (render(request, 'home.html', {'people' : people}))