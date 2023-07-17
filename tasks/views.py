from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Global dummy tasks
# tasks = ["foo", "bar", "baz"]
# tasks = []

# Form class to get access to the built in form
# Can define the required field. 
# We can provide constrains and client-side validation also gets applied here
class NewTaskForm(forms.Form):
   task = forms.CharField(label="New Task")
   # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
   if "tasks" not in request.session:
      request.session["tasks"] = []

   return render(request, "tasks/index.html", {
      "tasks": request.session["tasks"]
      # "tasks": tasks
   })

# def add(request):
#    return render(request, "tasks/add.html")

def add(request):
   if request.method == "POST":
      form = NewTaskForm(request.POST)
      if form.is_valid():
         task = form.cleaned_data["task"]
         request.session["tasks"] += [task]
         # tasks.append(task)
         return HttpResponseRedirect(reverse("tasks:index"))
      else:
         return render(request, "tasks/add.html", {
            "form": form
         })
      
   return render(request, "tasks/add.html", {
      "form": NewTaskForm()
   })

