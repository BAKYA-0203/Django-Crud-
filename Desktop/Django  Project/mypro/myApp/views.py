from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
#from django.db.models import F, Func
from django.db.models.functions import Sin

# Create your views here.

#def cal(request):
    #return render(request,"cal.html",{})

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            elif opr=="sin":
                c=Vector.objects.annotate(Sin(90)).get()
    except:
        c="Invalid opr....."
    print(c)
    return render(request,"calculator.html",{'c':c})

