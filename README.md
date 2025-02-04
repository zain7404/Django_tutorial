Getting Started with Django
What is Django?
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.

Django is a full-featured web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a set of tools and libraries for building web applicationss, including an ORM, a templating engine, and a built-in admin interface.

Environment Setup
To get started with Django, you’ll need to install it on your computer. You can do this by running the following command in your terminal, after setting up a virtual environment:

Terminal window
python3 -m venv .venv

# for windows
# python -m venv .venv

# to activate the virtual environment
source .venv/bin/activate

# for windows
# .venv\Scripts\activate

This is regular way but these days I am using uv to manage virtual environment and other tools. It’s rediculously easy and fast.

Terminal window
# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv

# With Homebrew.
brew install uv

# to create a virtual environment
uv venv

# activation commands are same as above

# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate

Now for all installations, you can use uv pip install command. For example, to install Django, run the following command:

Terminal window
uv pip install django

uv pip install -r requirements.txt

Django Project
A Django project is a collection of settings and configurations that define the structure and behavior of a web application. It includes the code for the application, as well as the templates, static files, and other resources that make up the application.

To create a new Django project, you can use the following command:

Terminal window
django-admin startproject chaiaurdjango
cd chaiaurdjango

This will create a new directory called chaiaurdjango with the basic structure of a Django project.

Start a Django Server
To start the Django server, you can use the following command:

Terminal window
python manage.py runserver

This will start the server and make it accessible at http://localhost:8000.

Ignore the unapplied migrations warning. This is a common issue when starting a new Django project. We will address this in a later section.

Creating our first views
Create a new file called views.py in the chaiaurdjango directory. In this file, we will define a few views that are simple functions that return a response. We want to have home page, about page, and contact page. Each of these pages will return html content.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")

def about(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")

Now, let’s create a new file called urls.py in the chaiaurdjango directory. In this file, we will define the URL patterns for our application. If the file is already there, you can just add the following code to the end of the file:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

Now, let’s run the server again and visit the following URLs:

http://localhost:8000/
http://localhost:8000/about/
http://localhost:8000/contact/
You should see the following output:

Welcome to Chai's Django Project: Home page
Welcome to Chai's Django Project: About page
Welcome to Chai's Django Project: Contact page

Adding Templates
In Django, templates are used to generate HTML pages. They are used to display data and perform logic in a web application. To create a template, you can create a new file called templates/index.html in the chaiaurdjango directory. Make sure that template folder is at same level as manage.py file. In this file, you can write HTML code that will be used to generate the HTML page.

<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Chai's Django Project</title>
</head>
<body>
    <h1>Welcome to Chai's Django Project</h1>
</body>
</html>

Now, let’s run the server again and visit the http://localhost:8000/ URL. You should see the following output:

Welcome to Chai's Django Project

Adding CSS and JavaScript
To add CSS and JavaScript to your Django project, you can create a new file called static/css/style.css in the chaiaurdjango directory. In this file, you can write CSS code that will be used to style the HTML page. You can also create a new file called static/js/script.js in the chaiaurdjango directory. In this file, you can write JavaScript code that will be used to add interactivity to the HTML page.

body {
  background-color: #161616;
  font-family: Arial, sans-serif;
  color: #fff;
}

console.log("Hello, world!");

To add this css file go to settings.py and add the following line:

import os # at the top of settings.py
'DIRS': ['templates'], # inside template section

STATIC_URL = '/static/' # below this add the following line
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

In the index.html file, add the following line:

at the top of the file:

{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">

Now, let’s change the home view to use the new template:

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

Now, let’s run the server again and visit the http://localhost:8000/ URL. You should see the following output:

Welcome to Chai's Django Project

Conclusion
This is the end of the first part of the tutorial. We will surely have more fun in the next part. Subscribe to our youtube channel to get notified about the next part of the tutorial. Keep enjoying Tea and Django!



Jinja Templates App in Django
Introduction
Jinja2 is a template engine for Python. It is used in Django to render templates. It is a very powerful template engine that can be used to render HTML, XML, and other formats. It is also used to render templates for the Django admin interface.

Installation
If you are in Django, you don’t need to install Jinja2 separately. It is already installed with Django. Django also comes with a built-in template configurations that allows you to use Jinja2 templates.

Jinja2 templates are written in a simple text format called HTML. The syntax is very similar to HTML, but with some additional features. You need to inject variables into the template using the {{ variable }} syntax. For example, if you want to display a name, you can use the following code:

Hello {{ name }}!

This will display the name of the person who is currently logged in, if there is one.

Common Template Tags
% if %
The {% if %} tag is used to conditionally display content in a template. It takes a boolean expression as an argument, and if the expression evaluates to True, the content inside the tag will be displayed. If the expression evaluates to False, the content will be skipped.

For example, the following code will display a greeting message only if the name variable is not empty:

{% if name %}
    Hello, {{ name }}!
{% endif %}

{% for %}
The {% for %} tag is used to iterate over a sequence of items. It takes a variable name and a sequence as arguments, and displays the content inside the tag for each item in the sequence.

For example, the following code will display a list of names:

{% for name in names %}
    {{ name }} is a name.
{% endfor %}

{% block %}
The {% block %} tag is used to define a block of content that can be overridden in child templates. It takes a name as an argument, and defines a block with that name that can be overridden in child templates.

For example, the following code defines a base template that includes a header and a footer:

<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    {% block content %}
        <h1>Welcome to my website!</h1>
    {% endblock %}
    <footer>
        {% block footer %}
            <p>Copyright © 2021</p>
        {% endblock %}
    </footer>
</body>
</html>

And the following code defines a child template that overrides the content block:

{% extends "base.html" %}

{% block title %}My Website{% endblock %}

{% block content %}
    <h1>Welcome to my website!</h1>
    <p>This is a child template.</p>
{% endblock %}

In this example, the content block in the child template overrides the content block in the base template, and the title block is not overridden.

{% include %}
The {% include %} tag is used to include the contents of another template file. It takes a template name as an argument, and includes the contents of the template file in the current template.

For example, the following code includes the contents of a template file called header.html:

{% include "header.html" %}

This will include the contents of the header.html template file in the current template.

{% extends %}
The {% extends %} tag is used to extend a base template. It takes a template name as an argument, and extends the base template with the contents of the template file.

For example, the following code extends the base.html template with the contents of a template file called child.html:

{% extends "base.html" %}

{% block content %}
    <h1>Welcome to my website!</h1>
    <p>This is a child template.</p>
{% endblock %}

In this example, the content block in the child template overrides the content block in the base template, and the title block is not overridden.

{% load %}
The {% load %} tag is used to load a template tag library. It takes a library name as an argument, and loads the template tag library with that name.

For example, the following code loads the static template tag library:

{% load static %}

This will load the static template tag library, which provides a set of template tags for working with static files.

{% static %}
The {% static %} tag is used to include a static file in a template. It takes a file path as an argument, and includes the contents of the file in the current template.

For example, the following code includes the contents of a CSS file called style.css:

<link rel="stylesheet" href="{% static 'style.css' %}">

This will include the contents of the style.css file in the current template.

{% url %}
The {% url %} tag is used to generate a URL for a view. It takes a view name and a set of arguments as arguments, and generates a URL for the view with those arguments.

For example, the following code generates a URL for the index view with the name argument set to 'John':

<a href="{% url 'index' name='John' %}">Go to the home page</a>

This will generate a link to the home page with the name argument set to 'John'.

Apps in Django
The most common way to organize your Django project is to use apps. An app is a self-contained module that contains models, views, templates, and other components of your project. Apps allow you to organize your code into logical units and make it easier to manage and maintain your project.

You can create it manually or use the startapp command to create a new app for you. To create an app, navigate to the directory where you want to create the app and run the following command:

Terminal window
python manage.py startapp chai

This will create a new directory called chai with the necessary files and directories for an app.

To add an app to your project, you need to add it to the INSTALLED_APPS setting in your project’s settings.py file. You can do this by adding the app’s name to the list of installed apps:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chai',
]

This will add the chai app to your project’s installed apps.

Templates in Apps and layout extension
In Django, templates are organized into apps. Each app can have its own templates directory, which contains the templates for that app. Create a new directory called templates in your app’s directory. Inside the chai directory, create a templates directory and add a all_chai.html file to it.

Add your basic html code to the all_chai.html file.

To serve this file, we need a view and a url. Create a new file called views.py in your app’s directory. Add the following code to the file:

from django.shortcuts import render

def all_chai(request):
    return render(request, 'all_chai.html')

This view will render the all_chai.html template when it is called.

Create a new file called urls.py in your app’s directory. Add the following code to the file:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
]

This urlpattern will map the root URL of the app to the all_chai view.

Now, we need to make aware of this new urlpattern in our project’s urls.py file. Add the following code to the project’s urls.py file:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chai/', include('chai.urls')),
]

This will include the chai.urls file in the project’s urlpatterns.

Now, we can access the all_chai view by going to http://localhost:8000/chai/.

Common Layout for all pages
In Django, you can create a common layout for all pages in your project by using the base.html template. Create a new file called base.html in your project’s templates directory. Add the following code to the file:

{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'style.css' %}">

  <title>
    {% block title %}
      Chai aur Django
    {% endblock title %}
  </title>
</head>
<body>
  <nav>I will add it later</nav>
  {% block content %}
  {% endblock %}
</body>
</html>

Now, this layout can be used for all pages in your project. To use it, you need to include it in your templates. For example, if you want to use the layout for the all_chai view, you can add the following code to the all_chai.html file:

{% extends "base.html" %}

{% block title %}
  All Chai
{% endblock %}

{% block content %}
  <h1>All Chai</h1>
  <p>This is the all chai page.</p>
{% endblock %}

This will use the base.html layout and override the title and content blocks with the appropriate values for the all_chai view.

Conclusion
In this part, we learned about Jinja2 templates and how to use them in Django. We also learned about apps in Django and how to create a common layout for all pages in your project. By using Jinja2 templates and apps, you can create dynamic and reusable templates in Django that make your web development process more efficient and enjoyable.

Tailwind to Django
Install Tailwind CSS in your Django project
How to add tailwind to your Django project and Django Admin

Tailwind CSS is a CSS framework that allows you to build custom styles for your web pages. It provides a set of pre-built classes that you can use to style your HTML elements.

Before we run the next command we need pip to be installed in your system. So far, we have been using uv to install packages, which is new and not yet supported by many packages.

Terminal window
python -m ensurepip --upgrade

# alternatively
python -m pip install --upgrade pip

To install Tailwind CSS in your Django project, you can use the following steps:

Terminal window
pip install django-tailwind
pip install 'django-tailwind[reload]'

This will install the django-tailwind package and the django-tailwind[reload] package, which includes the tailwind-django command-line tool.

Once you have installed Tailwind CSS, you can use the tailwind-django command to generate the necessary files for your project. This command will create a tailwind.config.js file in your project directory, as well as a static/css/tailwind.css file that contains the compiled Tailwind CSS.

Now, add tailwind to your INSTALLED_APPS in your settings.py file:

INSTALLED_APPS = [
    # ...
    'tailwind',
    # ...
]

Next, run the tailwind-django command to generate the necessary files for your project:

Terminal window
python manage.py tailwind init

Add the newly create theme to your INSTALLED_APPS in your settings.py file:

INSTALLED_APPS = [
    # ...
    'theme',
    # ...
]
TAILWIND_APP_NAME = 'theme' # This is the name of the app that will be used to generate the tailwind files
INTERNAL_IPS = ['127.0.0.1']

Now run the following command to generate the necessary files for your project:

Terminal window
python manage.py tailwind install

You can now use the Tailwind CSS classes in your Django templates. All though, tailwind provides you a base template that you can use to start your project but you can now use tailwind in any base template you want.

{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>

☕️ I was not able to get tailwind intellisense to work in my IDE, so I had to create a tailwind.config.js file manually. This file is totally empty but works

Finally, suggestions are there but you are not getting the desired result. That’s because this app needs nodejs to be installed in your system. And you need to provide the path to the nodejs executable in your settings.py file: You can use command which node to find the path to the nodejs executable.

NPM_BIN_PATH = '/usr/local/bin/npm'

# for windows
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

Now everything is ready and we need 2 terminals to run the app.

First terminal:

Terminal window
python manage.py runserver

Second terminal:

Terminal window
python manage.py tailwind start

for production change this command to python manage.py tailwind build

Hot Reloading
Since we have already installed the django-tailwind[reload] package, we can use the tailwind-django command to enable hot reloading in our project.

Add it to your INSTALLED_APPS in your settings.py file:

INSTALLED_APPS = [
    # ...
    'django_browser_reload',
    #...
]

Add following code to your settings.py file:

MIDDLEWARE = [
  # ...
  "django_browser_reload.middleware.BrowserReloadMiddleware",
  # ...
]

Add following code to your urls.py file:

from django.urls import include, path
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]

Enable the admin panel in Django
Now that we have Tailwind CSS installed and configured, we can enable the admin panel in our Django project. All settings and urls for the admin panel are already provided in django.

First run the migrate command to create the necessary tables for the admin panel:

Terminal window
python manage.py migrate

Next is to create the admin user:

Terminal window
python manage.py createsuperuser

Add your username, email (this can be empty), and password to the createsuperuser command.

Now you can acces the admin panel by going to http://localhost:8000/admin/ in your browser. Enter your username and password to log in.

Take a tour of the admin panel and in case you are wondering, yes, we can change the look and feel of the admin panel using so many plugins and themes that are available in the market but that is out of the scope of this tutorial.