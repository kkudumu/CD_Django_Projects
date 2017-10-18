from django.shortcuts import render, HttpResponse, redirect
import random
  # the index function is called when root is visited
x = []

def index(request):
    random = 0
    return render(request, "django_ninja_gold/index.html")

def money(request):
    try:
        request.session["activities"]
    except:
        request.session["activities"] = []
    
    try:
        request.session["gold"]
    except:
        request.session["gold"] = 0
    
    if request.POST["building"] == "farm":
        gold = random.randrange(9, 21)
        print "You harvested {} gold. Awesome!".format(gold)
    elif request.POST["building"] == "cave":
        gold = random.randrange(4, 11)
        print "You mined {} gold. Awesome!".format(gold)
    elif request.POST["building"] == "house":
        gold = random.randrange(1, 6)
        print "You housed {} gold. Awesome!".format(gold)
    elif request.POST["building"] == "casino":
        gold = random.randrange(-51, 51)
        print "You casinoed {} gold. Awesome!".format(gold)
    request.session["gold"] += gold
    global x
    request.session["activities"] = x
    x.append(["You made/lost " + str(gold) + " gold you're a cool person!"])
    return redirect("/")
    
