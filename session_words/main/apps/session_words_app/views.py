from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited
def index(request):
    try:
        request.session["add_word"]
    except: 
        request.session["add_word"] = []
    return render(request, "session_words_app/index.html")

def add_word(request):
    if 'font' in request.POST:
        font = '200%'
    else:
        font = '100%'

    context = {
        "word": request.POST.get("word"),
        "color": request.POST.get("choose_color"),
        "font": font,
        "time": strftime("%I:%M:%S %p, %B %d %Y ", gmtime())
    }

    request.session["add_word"].append(context)
    request.session.modified = True
    print request.session["add_word"]
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")