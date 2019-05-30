from django.shortcuts import render, redirect
from .models import Ewhaclass
import csv

def home(request):
    return render(request, 'home.html')

def csvsave(request):
    with open("LikeLion_Engclass.csv", 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            ewhaclass = Ewhaclass()
            ewhaclass.courseno = row[0]
            ewhaclass.classno = row[1]
            ewhaclass.title = row[2]
            ewhaclass.classification = row[3]
            if(row[4] == ''):
                ewhaclass.instructor = " "
            else:
                ewhaclass.instructor = row[4]
            ewhaclass.credit = row[5]
            ewhaclass.hour = row[6]
            ewhaclass.save()
    classes = Ewhaclass.objects
    return render(request, 'home.html', {'classes' : classes })

def filter(request):
    classification = request.GET['classification']
    classes = Ewhaclass.objects.filter(classification = classification)
    return render(request, 'home.html', {'classes' : classes})

# Create your views here.
