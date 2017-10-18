from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, "amadon_app/index.html")

def buy(request):
    request.session["total"] = 0

    try:
        request.session["count"]
    except:
        request.session["count"] = 0
    
    try:
        request.session["spent"]
    except:
        request.session["spent"] = 0

    if request.POST["product_id"] == "1015":                                #if statement to call our product ID
        price = 19.99 * int(request.POST["amount"])                         #setting our price to be multiplied by selected amount
        request.session["total"] += price                                   #adding the cost of user input to our running total
        request.session["count"] += int(request.POST["amount"])             #set our running count for the amount of items user purchased
        request.session["spent"] += price                                   #setting the spent amount spent to our price variable

    if request.POST["product_id"] == "1016":                                #equation will stay the same. just need to reference different product ID
        price = 29.99 * int(request.POST["amount"])                         #need to change value of price for each item
        request.session["total"] += price 
        request.session["count"] += int(request.POST["amount"])
        request.session["spent"] += price

    if request.POST["product_id"] == "1017":
        price = 4.99 * int(request.POST["amount"]) 
        request.session["total"] += price 
        request.session["count"] += int(request.POST["amount"])
        request.session["spent"] += price 

    if request.POST["product_id"] == "1018":
        price = 49.99 * int(request.POST["amount"]) 
        request.session["total"] += price 
        request.session["count"] += int(request.POST["amount"]) 
        request.session["spent"] += price 

    return redirect("/checkout")

def checkout(request):
    return render(request, "amadon_app/checkout.html")

def goback(request):
    return redirect("/")

#let's think this out. Things that are given:
# We will have 4 different items.
# We will need to process a quantity of 3 for each.
# We need to count the amount of items in the list the user ordered
# We need to sum the price of their previous items to say how much the user spent
# Can we make sum(request.post["price"])????