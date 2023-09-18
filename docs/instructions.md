**Env:**  
```
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```

**Start djangoapi Project:**  
```
django-admin.py startproject djangoapi
```

GOTO: djangoapi/djangoapi/settings.py and add 'rest_framework' to INSTALLED_APPS list:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'rest_framework',
]
```

Apply any pending database migrations and update the database schema to match the current state of your Django project.
```
cd djangoapi 
python manage.py migrate
```
start up a development server for this specific Django project:
```
python manage.py runserver
```

**Start app:**
```  
python manage.py startapp courses
```

```
$ pwd
django/djangoapi
```
```
$ ls -l
drwxrwxr-x. 1 oviner oviner    122 Aug 31 16:44 courses [new!!]
-rw-r--r--. 1 oviner oviner 131072 Aug 31 16:34 db.sqlite3
drwxrwxr-x. 1 oviner oviner    108 Aug 31 16:34 djangoapi
-rwxrwxr-x. 1 oviner oviner    665 Aug 31 16:28 manage.py
```

GOTO: djangoapi/djangoapi/settings.py and add 'courses' to INSTALLED_APPS list:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'rest_framework',
    'courses',
]
```

Add urls.py to courses:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

**Django admin Area:**  
Create super user:
$ python manage.py createsuperuser

Login sever
$ python manage.py runserver
http://127.0.0.1:8000/admin


**Create Models:** 
Create models for DB: 
```
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
```
makemigrations is the first step in making changes to your Django project's database schema. 
It generates migration files based on changes to your models.
```
(venv) oviner:djangoapi$ python manage.py makemigrations
No changes detected
```
Change Model:
```
(venv) oviner:djangoapi$ python manage.py makemigrations
Migrations for 'courses':
  courses/migrations/0002_alter_course_price.py
    - Alter field price on course
```
Apply Migrations: After creating migration files, you need to apply them to the database using the migrate command:
```
$ python manage.py migrate

```

**Add our model to the admin area:**    
https://docs.google.com/drawings/d/1tusD3OO4UMDmVDpK6TRlEGonUlTT5w4rHWRuSqN1NFQ/edit


**Create Views:**  
```
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
```


```
$ curl http://127.0.0.1:8000/courses

[{"id":1,"name":"Python Programming","language":"Python","price":"33"},{"id":2,"name":"Java Programming","language":"Java","price":"54"},{"id":3,"name":"C Programming","language":"C","price":"55"}]
```
