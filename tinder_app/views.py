from django.shortcuts import render
from . models import *



def home(request):
	dogs = Dog.objects.all()

	return render(request, 'tinder_app/home.html', {'dogs':dogs})




def details(request, pk):
	dogs_details = Dog.objects.filter(pk=pk)

	return render(request, 'tinder_app/details.html', {'dogs_details':dogs_details})