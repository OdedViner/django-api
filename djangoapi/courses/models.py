from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=11)
    level = models.CharField(max_length=30,default='Beginners')

    def __str__(self):
        return self.name
    
class Test(models.Model):
    test_name = models.CharField(max_length=200)
    test_logs = models.CharField(max_length=200)
    test_status = models.CharField(max_length=200)
    def __str__(self):
        return self.test_name