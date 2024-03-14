from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from first.forms import NameAgeForm

# Create your views here.
## app.get("/hello", (req, res) => res.send("Hello World"))

## Basic Route
def hello(request):
    return HttpResponse("Hello World")

## Route Using Params
def add(request, num1, num2):
    return HttpResponse(f"{num1 + num2}")

## Route Using Query Params
def add2(request):
    ## GET property on the request is a dictionary of query params
    num1 = int(request.GET.get("num1", 5))
    num2 = int(request.GET.get("num2", 6)) 
    return HttpResponse(f"{num1 + num2}")

## Route using a Template
def our_index(request):
    if(request.method == "GET"):
        ## Create a Copy of the Form
        form = NameAgeForm()
        print(form)
        ## res.render("first/index.ejs", {cheese: "gouda"})
        return render(request, "first/index.html", {"cheese": "gouda", "nums": [1,2,3,4,5], "form": form})
    if(request.method == "POST"):
        print(request.POST)
        name = request.POST.get("name")
        age = request.POST.get("age")
        return JsonResponse({"name": name, "age": age })

## Route that returns a JSON response
def jaysun(request):
    ## res.json()
    return JsonResponse({"hello": "Hello World"})