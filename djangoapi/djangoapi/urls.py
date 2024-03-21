from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('courses.urls')),
    path('courses/<int:test_id>/', views.test_deatil, name='test_deatil'),
    path('courses/tests/', views.test_deatil_new, name='test_deati_new'),

]
