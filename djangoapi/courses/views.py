from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
from .models import Course
from .models import Test
from .serializers import CourseSerializer

#viewsets provides the base classes for creating API views that perform CRUD 
# (Create, Read, Update, Delete) operations on your data models.
class CourseView(viewsets.ModelViewSet):
    # creating a queryset for the Django model named Course. 
    # This line of code is a common way to retrieve all records 
    # from the database associated with the Course model.
    queryset = Course.objects.all()
    # This is an attribute you set in a DRF view or viewset to specify which 
    # serializer class should be used for serializing and deserializing data when processing HTTP requests.
    serializer_class = CourseSerializer

def test_deatil(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
    except Test.DoesNotExist:
        raise Http404("test_id not found")
    # return HttpResponse(f"<p>deatil view with id {test_id}</p>")
    return render(request, 'test_detail.html', {
        'test':test,
    })

def test_deatil_new(request):
    test = Test.objects.all()
    return render(request, 'test_deatil_new.html', {
        'tests':test,
    })

