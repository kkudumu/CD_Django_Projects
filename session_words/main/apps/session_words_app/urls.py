from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^add_word$', views.add_word),     # This line has changed!
    url(r'^clear$', views.clear)     # This line has changed!
  ]