from django.shortcuts import render
from .models import Destination
def index(request):
    desc=Destination.objects.all()
    return render(request,'index.html',{"destination":desc})
# Create your views here.
