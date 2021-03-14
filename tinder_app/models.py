from django.db import models
from django_resized import ResizedImageField
from datetime import datetime



class DogBreed(models.Model):
	breed = models.CharField(max_length=50)

	def __str__(self):
		return self.breed



class Dog(models.Model):
	breed = models.ForeignKey('DogBreed', on_delete=models.CASCADE)
	gender = models.CharField(max_length=10)
	birthYear = models.CharField(max_length=15)
	info = models.TextField(max_length=1000)
	date = models.DateTimeField(default=datetime.now, blank=True)
	image = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True)
	image2 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image3 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image4 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image5 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image6 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)

	def __str__(self):
		return (f'{self.birthYear}, {self.gender}, {self.breed}, {self.date}')

	class Meta:
		ordering = ['-date']