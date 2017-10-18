"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#WE DEFINE WHERE TO GO ON THIS ONE!!
from django.conf.urls import url, include # Notice we added include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.django_app.urls')) # And now we use the include function to pull in our first_app.urls...
    # url(r'^create', include('apps.django_app.urls')), 
    # url(r'^new', include('apps.django_app.urls')),
    # url(r'^(?P<number>\d+)', include('apps.django_app.urls')),
    # url(r'^(?P<number>\d+)/edit', include('apps.django_app.urls')), THESE ARE MISTAKES. DON'T NEED THIS INFO. KEEPING HERE TO TEACH SELF A LESSON
    # url(r'^(?P<number>\d+)/delete', include('apps.django_app.urls'))
  ]
