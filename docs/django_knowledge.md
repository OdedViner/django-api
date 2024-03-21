<h2>Creating a project:</h2>
```
django-admin startproject mysite
```

```  
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```  

The outer mysite/:
root directory is a container for your project. 

manage.py: 
A command-line utility that lets you interact with this Django project

The inner mysite/ directory: 
The actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

mysite/__init__.py: 
An empty file that tells Python that this directory should be considered a Python package. 

mysite/settings.py: 
Settings/configuration for this Django project. 

mysite/urls.py: 
The URL declarations for this Django project; a “table of contents” of your Django-powered site.

mysite/asgi.py: 
An entry-point for ASGI-compatible web servers to serve your project.

mysite/wsgi.py: 
An entry-point for WSGI-compatible web servers to serve your project


*Creating the Polls app*

<h2>Creating the Polls app</h2>
To create your app:
```
$ python manage.py startapp polls
```

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```


<h3>Models:</h3>
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

Add to INSTALLED_APPS list: 
A list of strings designating all applications that are enabled in this Django installation.
The default settings.py file created by django-admin startproject sets
For example:
```
INSTALLED_APPS = [
    'rest_framework',
    'courses',
]
```

Relationships:
Clearly, the power of relational databases lies in relating tables to each other. Django offers ways to define the three most common types of database relationships: many-to-one, many-to-many and one-to-one.

Making queries:
Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects.

```
$ python manage.py shell
>>> from courses.models import Course
>>> a=Course(name="Java Script Course", language="Java Script", price="333")
>>> a.save()
>>> all_entries = Course.objects.all()
>>> all_entries
<QuerySet [<Course: C Programming>, <Course: Java Script Course>]>
```

