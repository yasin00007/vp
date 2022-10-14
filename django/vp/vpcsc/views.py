from django.shortcuts import render,HttpResponse
from datetime import datetime
from vpcsc.models import vpcsc_contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    return render(request,'index.html')

def about_1(request):
    return render(request,'about_1.html')
def about_2(request):
    return render(request,'about_2.html')
def about_3(request):
    return render(request,'about_3.html')        


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        desc = request.POST.get('desc') 
        contact = vpcsc_contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request,'contact.html')


def bcs(request):
    return render(request,'bcs.html')
def bca(request):
    return render(request,'bca.html')
def bba(request):
    return render(request,'bba.html') 

def photo(request):
    return render(request,'photo.html')
def video(request):
    return render(request,'video.html')    

def facilities(request):
    return render(request,'facilities.html') 

def eligibility(request):
    return render(request,'eligibility.html') 
def required_documents(request):
    return render(request,'required_documents.html')


def placement(request):
    return render(request,'placement.html')


def sports(request):
    return render(request,'sports.html') 
def nss(request):
    return render(request,'nss.html')

def library(request):
    return render(request,'library.html')
def syllabi(request):
    return render(request,'syllabi.html')
def exami(request):
    return render(request,'exami.html')  
def results (request):
    return render(request,'results.html')
def scholarships(request):
    return render(request,'scholarships.html')    
def student_helpline(request):
    return render(request,'student_helpline.html')    



