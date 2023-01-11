from django.shortcuts import render
from.forms import Studentregistration

# Create your views here.
def show(request):
    fm=Studentregistration()
    return render(request,"enrolls/index.html",{"form":fm})
