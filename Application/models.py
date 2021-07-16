from django.db import models

# Create your models here.

class Sketch(models.Model):
	title = models.CharField(max_length = 100)
	images = models.ImageField(upload_to = 'Application/Sketch')
	description = models.TextField()
	def __str__(self):
		return self.title
	
class Nature(models.Model):
	title = models.CharField(max_length = 100)
	images = models.ImageField(upload_to = 'Application/Nature')
	description = models.TextField()
	def __str__(self):
		return self.title
		
class Portrait(models.Model):
	title = models.CharField(max_length = 100)
	images = models.ImageField(upload_to = 'Application/Portrait')
	description = models.TextField()
	def __str__(self):
		return self.title
		
class Cars(models.Model):
	title = models.CharField(max_length = 100)
	images = models.ImageField(upload_to = 'Application/Cars')
	description = models.TextField()
	def __str__(self):
		return self.title
		
class Wildlife(models.Model):
	title = models.CharField(max_length = 100)
	images = models.ImageField(upload_to = 'Application/Wildlife')
	description = models.TextField()
	def __str__(self):
		return self.title
		

	
