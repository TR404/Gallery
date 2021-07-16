"""Gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from Application import views

urlpatterns = [
    path('developer/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('sketch/', views.sketch, name = 'sketch'),
    path('nature/', views.nature, name = 'nature'),
    path('portrait/', views.portrait, name = 'portrait'),
    path('cars/', views.cars, name = 'cars'),
    path('wildlife', views.wildlife, name = 'wildlife'),
    path('sketchImages/<int:imageId>/',views.sketchImages, name = 'sketchImages'),
    path('natureImages/<int:imageId>/',views.natureImages, name = 'natureImages'),
    path('portraitImages/<int:imageId>/',views.portraitImages, name = 'portraitImages'),
    path('carsImages/<int:imageId>/',views.carsImages, name = 'carsImages'),
    path('wildlifeImages/<int:imageId>/',views.wildlifeImages, name = 'wildlifeImages'),
	path('search/', views.searchbar, name = 'searchbar'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
