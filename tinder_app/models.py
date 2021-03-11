from django.db import models
from django_resized import ResizedImageField



class DogBreed(models.Model):
	breed = models.CharField(max_length=50)

	def __str__(self):
		return self.breed



class Dog(models.Model):
	image = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True)
	birthYear = models.CharField(max_length=15)
	gender = models.CharField(max_length=10)
	info = models.TextField(max_length=1000)
	breed = models.ForeignKey('DogBreed', on_delete=models.CASCADE)

	def __str__(self):
		return (f'{self.birthYear}, {self.gender}, {self.breed}')