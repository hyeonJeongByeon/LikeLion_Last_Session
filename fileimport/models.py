from django.db import models

class Ewhaclass(models.Model):
    courseno = models.CharField(max_length = 10)
    classno = models.CharField(max_length = 5)
    title = models.CharField(max_length = 50)
    classification = models.CharField(max_length = 50)
    instructor = models.CharField(max_length = 50)
    credit = models.CharField(max_length = 10)
    hourt = models.CharField(max_length = 10)

    def __str__(self):
        return self.courseno

# Create your models here.


