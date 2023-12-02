from django.shortcuts import render,redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,login as djlogin

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def register(request):
    msg=None
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            msg="Success"
            return redirect("login")
        else:
            msg="Error"
    
    else:
        form=SignUpForm()
    
    return render(request,"register.html",{'form':form,'msg':msg})


def login(request):
    form=LoginForm(request.POST or None)
    msg=None
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None and user.is_admin:
                djlogin(request,user)
                return redirect('adminuser')
            elif user is not None and user.is_employee:
                djlogin(request,user)
                return redirect('employee')
            elif user is not None and user.is_customer:
                djlogin(request,user)
                return redirect('customer')
            elif user is not None and user.is_student:
                djlogin(request,user)
                return redirect('student')
            else:
                msg="Invalid Credentials"
    
    return render(request,"login.html",{'form':form,'msg':msg}) 


def adminuser(request):
    return render(request,"adminuser.html",{})

def customer(request):
    return render(request,"customer.html",{})

def employee(request):
    return render(request,"employee.html",{})  

def student(request):
    return render(request,"student.html",{})           