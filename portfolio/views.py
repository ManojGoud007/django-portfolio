from django.shortcuts import render
from .models import Project, Skills
# Create your views here.

def home(request):
    projects = Project.objects.all()
    skills =  Skills.objects.all()
    context = {
        'projects':projects,
        'skills':skills
    }
    return render(request,'portfolio/home.html',context)
