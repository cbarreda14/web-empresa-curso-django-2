from django.shortcuts import render
from .models import project

# Create your views here.
def service(request):
    services = project.objects.all()
    return render(request,'services/services.html',{'services':services})