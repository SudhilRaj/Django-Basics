# Django-Basics

* Django is a Python framework in order to create dynamic web applications.
* Django is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that, a lot of code is already written for us that we can take advantage of.

* To install Django, run-> ```pip install Django``` - LTS - 4.2  (We’ll also have to install pip if we haven’t already done so) 

* For creating a new project, run -> ```django-admin startproject PROJECT_NAME``` (Here our project name is 'djtest')
	- We can see number of starter files. There are three files that will be very important from the start:
	1) ```manage.py``` -  is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
	2) ```settings.py``` - contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them 	from time to time (Like adding new application definition).
	3) ```urls.py``` - contains directions for where users should be routed after navigating to a certain URL.

* To start the project -> ```python manage.py runserver```
	- This will open a development server, which we can access by visiting the URL provided. This development server is being run locally on our machine, meaning other people cannot access our website. This should bring us to a default landing page.

* Every Django project generally consist of one or more Django applications. (Based on the requirements)

* To creare a Django application, run -> ```python manage.py startapp app-name```
	- This will create a new app directory in the project folder along with the existing starter files. The new directory also consist of multiple starter files with initial configuration.
* To install the newly created app to the project:
	- Go to the ```settings.py``` file and configure the new app under the ```INSTALLED_APPS``` section. This section is where the Django configure what apps are installed on the project. (There should be some default apps)

* Lets create a new app called 'hello' in the 'djtest' project.
* Look into ```hello/views.py``` file:
	- Each view is something what the user want to see. To create a view we need to define a function.
	- Eg:

``` python
from django.http import HttpResponse
from django.shortcuts import render

  # Create your views here.
  def index(request):
        return HttpResponse("Hello World")

  def sudhil(request):
      return HttpResponse("Hello, Sudhil!")

  def anu(request):
      return HttpResponse("Hello, Anu!")

  # Making the function general or parametarising.
  def greet(request, name):
      return HttpResponse(f"Hello, {name.capitalize()}!")
  ```

* We can create as many views as required by creating the functions.
* For each views, we need a route to define when will a particular view should display.
* For defining the app routes, we need to create a separate ```urls.py``` file for the particular app.(The project already have a main ```urls.py``` file)
	- Eg: ```hello/urls.py```
``` python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #Default route
    path("sudhil", views.sudhil, name="sudhil"),
    path("anu", views.anu, name="anu"),
    path("<str:name>", views.greet, name="greet") #A general route with a parameter.(Custom route. Here it will deal any string as a parameter)
  ]
```

* As a last thing, inorder to work everything correctly, go the main ```urls.py``` in the project and register the new urls for the app. That file is the master url file for the entire project or all of the applications within the project.
	- Eg:
``` python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
      path('admin/', admin.site.urls),
      path('hello/', include("hello.urls")),
]
```

* All set! now if we go to http://127.0.0.1:8000/hello/qwerty
	we will get "Hello, Qwerty!" as the response.

* Now in the views, we are just returning the texts/strings as the HTTP response. But these HTTP responses can be any HTML content. Even we can send an entire HTML page.

* The way we can do that is, instead of returning an HTTP response, we can render a template.
	- Eg: ```hello/views.py```
``` python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")
```
* ```hello/templates/hello/index.html```
 ``` html
<!DOCTYPE html>
<html lang="en">
    <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Hello</title>
    </head>
    <body>
          <h1>Hello, World template!</h1>
    </body>
</html>
```

* In this example our template is called ```index.html```. We need to create a directory called 'templates' inside the 'hello' app. Inorder to prefix the templates with the app name, we can also create a 'hello' directory inside the 'templates' directory. So our new template path will be ```templates/hello/index.html``` inside the hello app.
* Now, if we visit http://127.0.0.1:8000/hello/ (default route of the hello app), we can see the rendered index.html template.

* In the way we can directly render any html template using Django. Also, Django has added its own templating language on top of the existing HTML. So we can take that advantage and make the HTML templates more dynamic (That means, we can use more programming aspects on the HTML like variables, conditions, loops and other stuff). 

	- Eg: ```hello/views.py```
``` python
# Using a custom template
# Here the optional third argument is called 'context' (It is a python dict).
# It is all of the information need to provide to the template or the 
# template have access to, like variables.
def greet2(request, name):
    return render(request, "hello/greet2.html", {
          "name": name.capitalize()
     })
```

- In the ```greet2.html``` template we can get the variable using the ```{{ }}``` syntaxt of Django. By using this we can render the value of a dynamic variable. Here it will be like ```<h1>Hello, {{ name }}!</h1>```

	* ```hello/templates/hello/greet2.html```
``` html
<!DOCTYPE html>
  <html lang="en">
    <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Hello</title>
    </head>
    <body>
          <h1>Hello, {{ name }}!</h1>
    </body>
</html>
```

* Here many things are happening in many files but all the logic, routes, views and the templates are completely isolated.

* Django templating language has more other powerful features. (In fact we can use all the aspects of a programming language)
* Eg: Let's create a new app called 'newyear' that check whether the current date is new year or not. (Register the app and the app routes on the project. And do the necessary steps as previous).

* For the conditions Django use ```{% %}``` syntax.
	- Eg: ```newyear/views.py```
``` python
import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
          "newyear": now.month == 1 and now.day == 1
    })
```
  -   ```newyear/templates/newyear/index.html```
``` html
<!DOCTYPE html>
<html lang="en">
    <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>New Year?</title>
    </head>
    <body>
         <!-- <p>{{ newyear }}</p> -->
          {% if newyear %}
            <h1>YES</h1>
          {% else %}
            <h1>NO</h1>
          {% endif %}
    </body>
</html>
```

* We can also add the custom CSS. Django has a special build system to deal with the static files like CSS.
* We need to put the CSS files inside a directory in the newyear app called 'static'. (Eg: create ```newyear/static/newyear/styles.css```)
``` css
h1{
	font-family: sans-serif;
	font-size: 90px;
	text-align: center;
}
```

* On the top of the ```index.html``` page, we need to add ```{% load static %}```
* The link to the file will be, ```<link href="{% static 'newyear/styles.css' %}" rel="stylesheet">```
* This way of linking is better than directly putting the url.
* We can check the output by restarting the server.

* Let's create an another app for a todo list to use the above features and and some other features. (Create a new app called 'tasks'. Register the app and the app routes on the project. And do the necessary steps as previous).

1) ```tasks/urls.py```
``` python
from django.urls import path
from . import views

app_name = "tasks" #Unique app_mame for the urls in order to avoid namespace collision. But this version has no problem with namespacing.
urlpatterns = [
	path("", views.index, name="index"), #Default route
	path("add", views.add, name="add")
]
```

2) ```tasks/views.py```
``` python
from django.shortcuts import render

# Global dummy tasks
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
	return render(request, "tasks/index.html", {
		"tasks": tasks
	})

def add(request):
	return render(request, "tasks/add.html")
```

3) ```tasks/templates/tasks/layout.html```
``` html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Tasks</title>
	</head>
	<body>
		{% block body %}
		{% endblock %}
	</body>
</html>
```

5) ```tasks/templates/tasks/index.html```
``` python
{% extends "tasks/layout.html" %}

{% block body %}
	<h1>Tasks</h1>
	<ul>
		{% for task in tasks %}
		<li>{{ task }}</li>
		{% endfor %}
	</ul>
	<a href="{% url 'tasks:add' %}">Add a New Task</a>
{% endblock %}
```

7) ```tasks/templates/tasks/add.html```
``` python
{% extends "tasks/layout.html" %}

{% block body %}
	 <h1>Add Task</h1>
	 <form action="{% url 'tasks:add' %}" method="post">
		{% csrf_token %}
		<input type="text" name="task"/>
		<input type="submit" />
	</form>
	<a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```


* Template inheritance -  We can inherit the templates and avoid code duplication.
	- Here both the above ```index.html``` page and the ```add.html``` page have many things in common and they have only difference in their body. So we can create a common layout file called ```layout.html``` to inherit all the common content to other pages.
	- For linking to other routes from a template, we can use a link like below instead of directly specifying the 	route name.
		```<a href="{% url 'index' %}">View Tasks</a>```
	-> If there exist an ```app_name``` in the app route in order to avoid name sapce collision with other apps, we can specify that in the link ```<a href="{% url 'tasks:index' %}">View Tasks</a>```

* Now all the routes works well, but if we submit something on the add form it will throw some error.
	- 403 - CSRF verification failed
	- ```CSRF``` - Cross Site Request Forgery - Submitting fake data through forms - Security vulnerability.
	- We can use a csrf token to verify the form submission.
	- Django has csrf validation turned on by default through a specific add-on known as 'Django Middleware' (In ```settings.py``` file).
	- To validate, add ```{% csrf_token %}``` inside the particular form tag. It will add a hidden csrf token inside the form. The token will change each time based on the session.
	- If we look at the page source:
``` html
<form action="/tasks/add" method="post">
	<input type="hidden" name="csrfmiddlewaretoken" value="tA7puflcApWmiR4QZH3abjZDw5nZvP3yyIE50a8x7isDmVkoyuYV15AF3vv87cVg">
	<input type="text" name="task"/>
	<input type="submit" />
</form>
```

* Django also has built in tools for building the forms and validating data easier.

* Sessions - All information about a particular session. Here, if we set tasks in session, It will throw
``` python
OperationalError at /tasks/
no such table: django_session
````

* This is becuase Django stores all the data inside tables but right now that table does not exist.

* To create the tables or apply the migrations run- ```python manage.py migrate```
	- This command will allow us to create all of the default tables inside the Django's DB.

* For more information, refer the official Django documentation - https://docs.djangoproject.com/en/4.2/
