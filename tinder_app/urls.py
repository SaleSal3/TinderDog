from django.urls import path
from . import views



urlpatterns = [
	path('', views.home, name='home'),
	path('<pk>/details/', views.details, name='details'),
]