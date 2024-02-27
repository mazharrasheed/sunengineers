
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Contactus

from .forms import Contact_Form

# Create your views here.

def index(request):
    context={   'veriable1':"Mazhar is coder",
                'veriable2':"sheery is draftman"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is home page!")
def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is about page!")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page!")

def contact(request):
    data={}

    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        form=Contact_Form(request.POST)
        mycontact=Contactus(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        mycontact.save()
        messages.success(request,"Success! Your massage has been sent")
        form=Contact_Form()
    else: 
        form=Contact_Form()

    data={'form':form}
    return render(request,'contact.html',data)
    # return HttpResponse("This is contact page!")

def news(request):

    return render(request,'news.html')
    # return HttpResponse("This is contact page!")
def career(request):

    return render(request,'career.html')
    # return HttpResponse("This is contact page!")

def productfw(request):

    return render(request,'fixedwheel.html')
    # return HttpResponse("This is contact page!")

