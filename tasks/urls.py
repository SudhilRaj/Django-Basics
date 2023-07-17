from django.urls import path
from . import views

app_name = "tasks" #In order to avoid namespace collision. But this version has no problem with namespacing.
urlpatterns = [
   path("", views.index, name="index"), #Default route
   path("add", views.add, name="add")
]