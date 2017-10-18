from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, "survey_form_app/index.html")

def process(request):
    request.session["name"] = request.POST["name"] 
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]
    try:
        request.session["counter"] += 1
    except:
        request.session["counter"] = 1
    return redirect("/result")

def result(request):
    return render(request, "survey_form_app/result.html")