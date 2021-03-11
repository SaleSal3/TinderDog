from django.shortcuts import render
from . models import *



def home(request):
	dogs = Dog.objects.all()

	context = {'dogs':dogs}
	return render(request, 'tinder_app/home.html', context)