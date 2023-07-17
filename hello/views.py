from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Simple views
def index(request):
   return render(request, "hello/index.html")

def sudhil(request):
   return HttpResponse("Hello, Sudhil!")

def anu(request):
   return HttpResponse("Hello, Anu!")

# Making the function general or parametarising.
def greet(request, name):
   return HttpResponse(f"Hello, {name.capitalize()}!")

# Using a custom template
# Here the optional third argument is called 'context' (It is a python dict).
# It is all of the information need to provide to the template or the 
# template have access to, like variables.
def greet2(request, name):
   return render(request, "hello/greet2.html", {
      "name": name.capitalize()
   })
