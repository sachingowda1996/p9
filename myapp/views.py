from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.
def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def trail(request):
    return HttpResponse("<h1>project is on air</h1>")

def profile(request):
    name="sachinGowda"
    return render(request,"myapp/profile.html",{'name':name})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h4>factorial is {} </h4>".format(factorial(n)))  

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':'sachin','name':'nagesh'})

def fourth(request):
    fruits=['strawberry','cherry']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':1000})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def great_2_number(request,a,b):
    if a>b:
        return HttpResponse("the greatest value is {}".format(a))
    elif b>a:
        return HttpResponse("the greatest value is {}".format(b)) 
    else:
        return HttpResponse("all are equal") 

def reverse(request,a):
    b=''
    for i in a:
        b=i+b
        return HttpResponse(str(b))
                                      

