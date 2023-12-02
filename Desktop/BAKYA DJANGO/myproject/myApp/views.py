from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from.models import Employee


# Create your views here.

def home(request):
    return render(request,"home.html",{})

def addemp(request):
    if request.method=="POST":
        ename=request.POST.get("name")
        email=request.POST.get("email")
        epwd=request.POST.get("pwd")
        eaddr=request.POST.get("addr")
        e=Employee()
        e.name=ename
        e.email=email
        e.pwd=epwd
        e.addr=eaddr
        e.save()
    return render(request,"addemp.html",{})

def viewemp(request):
    e=Employee.objects.all()
    return render(request,"viewemp.html",{'emp':e})

def update(request,id):
    s=Employee.objects.get(pk=id)
    return render(request,"update.html",{'std':s})

def upemp(request,id):
    ename=request.POST.get("name")
    email=request.POST.get("email")
    epwd=request.POST.get("pwd")
    eaddr=request.POST.get("addr")

    e=Employee.objects.get(pk=id)
    e.name=ename
    e.email=email
    e.pwd=epwd
    e.addr=eaddr
    e.save()
    return redirect('home')


def delemp(request,id):
     s=Employee.objects.get(pk=id)
     s.delete()
     return redirect('home')

def profile1(request,id):
    s=Employee.objects.get(pk=id)
    return render(request,"profile.html",{'std':s})
    


