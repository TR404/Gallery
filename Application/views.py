from django.shortcuts import render
from .models import *
from .form import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from itertools import chain

# Create your views here.
def index(request):
	sketch = Sketch.objects.all()[::-1]
	nature = Nature.objects.all()[::-1]
	portrait = Portrait.objects.all()[::-1]
	cars = Cars.objects.all()[::-1]
	wildlife = Wildlife.objects.all()[::-1]
	orders = list(sorted(chain(sketch, nature, portrait, cars, wildlife),key=lambda objects: objects.title,reverse=True ))
	paginator = Paginator(orders, 9)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	return render(request, 'Application/index.html', {'pageObj': pageObj})
	
def sketch(request):
	sketch = Sketch.objects.all()
	paginator = Paginator(sketch, 8)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	if request.method == 'GET':
		return render(request, 'Application/sketch.html', {'pageObj': pageObj, 'form':SketchModel()})
	else:
		try:
			form = SketchModel(request.POST,request.FILES)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'Application/sketch.html', {'pageObj': pageObj, 'form':form, 'error':'Wrong Information Passed'})
	
	
def nature(request):
	nature = Nature.objects.all()
	paginator = Paginator(nature, 8)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	if request.method == 'GET':
		return render(request, 'Application/nature.html', {'pageObj': pageObj, 'form':NatureModel()})
	else:
		try:
			form = NatureModel(request.POST,request.FILES)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'Application/nature.html', {'pageObj': pageObj, 'form':form, 'error':'Wrong Information Passed'})
	
	
def portrait(request):
	portrait = Portrait.objects.all()
	paginator = Paginator(portrait, 8)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	if request.method == 'GET':
		return render(request, 'Application/portrait.html', {'pageObj': pageObj, 'form':NatureModel()})
	else:
		try:
			form = PortraitModel(request.POST,request.FILES)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'Application/portrait.html', {'pageObj': pageObj, 'form':form, 'error':'Wrong Information Passed'})
	

def cars(request):
	cars = Cars.objects.all()
	paginator = Paginator(cars, 8)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	if request.method == 'GET':
		return render(request, 'Application/cars.html', {'pageObj': pageObj, 'form':CarsModel()})
	else:
		try:
			form = CarsModel(request.POST,request.FILES)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'Application/cars.html', {'pageObj': pageObj, 'form':form, 'error':'Wrong Information Passed'})
	
	
def wildlife(request):
	wildlife = Wildlife.objects.all()
	paginator = Paginator(wildlife, 8)
	pageNumber = request.GET.get('page')
	pageObj = paginator.get_page(pageNumber)
	if request.method == 'GET':
		return render(request, 'Application/wildlife.html', {'pageObj': pageObj, 'form':WildlifeModel()})
	else:
		try:
			form = WildlifeModel(request.POST,request.FILES)
			form.save()
			return redirect('index')
		except ValueError:
			return render(request, 'Application/wildlife.html', {'pageObj': pageObj, 'form':form, 'error':'Wrong Information Passed'})
	
def sketchImages(request, imageId):
	image = get_object_or_404(Sketch, pk = imageId)
	return render(request, 'Application/sketchImages.html', {'image': image})
	
	

def natureImages(request, imageId):
	image = get_object_or_404(Nature, pk = imageId)
	return render(request, 'Application/natureImages.html', {'image': image})
	
	
def carsImages(request, imageId):
	image = get_object_or_404(Cars, pk = imageId)
	return render(request, 'Application/carsImages.html', {'image': image})
	
	
def portraitImages(request, imageId):
	image = get_object_or_404(Portrait, pk = imageId)
	return render(request, 'Application/portraitImages.html', {'image': image})
	
	
def wildlifeImages(request, imageId):
	image = get_object_or_404(Wildlife, pk = imageId)
	return render(request, 'Application/wildlifeImages.html', {'image': image})
	
	
def searchbar(request):
	search = request.GET['search']
	projects = Sketch.objects.filter(title__icontains=search) or Nature.objects.filter(title__icontains=search) or Cars.objects.filter(title__icontains=search) or Portrait.objects.filter(title__icontains=search) or Wildlife.objects.filter(title__icontains=search)
	return render(request, 'Application/searchbar.html', {'projects': projects, "search": search})
