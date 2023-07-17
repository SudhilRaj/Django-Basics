from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"), #Default route
   path("sudhil", views.sudhil, name="sudhil"),
   path("anu", views.anu, name="anu"),
   # path("<str:name>", views.greet, name="greet"), #A general route with a parameter.(Custom route. Here it will deal any string as a parameter)
   path("<str:name>", views.greet2, name="greet2")
]