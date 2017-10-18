from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
#WE CALL OUR METHODS ON THIS ONE!!
  
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    response = "placeholder to display blog {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog {}".format(number)
    return  HttpResponse(response)

def destroy(request, number):
    return redirect ("/")
/Users/kio/Desktop/CD_Django_Projects/django_app/main/apps/django_app/urls.py
