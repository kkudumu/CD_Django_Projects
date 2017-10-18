from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    try:
        request.session["counter"] += 1
    except:
        request.session["counter"] = 1
    try: 
        request.session["word"] = get_random_string(length=14)
    except: 
        request.session["word"] = 1
    return render(request,'random_word_app/index.html')

def reset(request):
    del request.session["counter"]
    return redirect('/')