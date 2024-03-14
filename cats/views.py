from django.shortcuts import render, redirect, HttpResponse
from cats.models import Cat
from cats.forms import CatForm
# Create your views here.

## /cats
def index_create(request):
    ## INDEX
    if(request.method == "GET"):
        ## fetch all cats from database
        cats = Cat.objects.all()
        ## render template with cats
        return render(request, "cats/index.html", {"cats": cats})
        
    ## CREATE
    if(request.method == "POST"):
        ## get the details from form
        name = request.POST.get("name")
        age = request.POST.get("age")
        legs = request.POST.get("legs")
        ## Create the cat
        Cat.objects.create(name=name, age=age, legs=legs)
        ## redirect back to index
        return redirect("/cats/")

## /cats/<id>
def update_delete_show(request):
    ## SHOW
    if (request.method == "GET"):
        return HttpResponse("pass")
    ## Update
    if (request.method == "PUT"):
        return HttpResponse("pass")
    ## Delete
    if (request.method == "DELETE"):
        return HttpResponse("pass")

## /cats/<id>/edit
def edit(request):
    return HttpResponse("pass")

# /cats/new
def new(request):
    ## Create a New CatForm
    form = CatForm()
    ## Send Form to Template
    return render(request, "cats/new.html", {"form": form})