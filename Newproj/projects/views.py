from django.shortcuts import render

# Create your views here.

def projects(request):
    return render(request,'projects/projects.html')

def single_project(request,pk):
    return render(request,'projects/single_project.html')