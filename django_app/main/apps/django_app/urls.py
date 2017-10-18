from django.conf.urls import url
from . import views           # This line is new!

#WE DO THE REGEX CALLS ON THIS ONE!!!!
urlpatterns = [
    url(r'^$', views.index),     
    url(r'^new$', views.new),     #CREATE URL PATH FOR /NEW
    url(r'^create$', views.create),    
    url(r'^(?P<number>\d+)$', views.show),     #NEED THIS DOLLAR SIGN HERE TO TELL DJANGO WE WANT MORE LINKS AFTER
    url(r'^(?P<number>\d+)/edit', views.edit),    
    url(r'^(?P<number>\d+)/destroy', views.destroy)     
  ]