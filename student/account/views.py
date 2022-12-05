from django.shortcuts import render,redirect
from .models import Contact,Staff,Course
from django.contrib import messages




# Create your views here.
def index(request):
    return render(request,'index.html')
def mainhome(request):
    return render(request,'mainhome.html')

def contact(request):
    if request.method == 'post':
        if request.post['name'] is not None:
            enq=Contact.objects.create(name=request.post['name'],email=request.post['email'],phno=request.post['phno'])
            enq.save()
            dicts={'out':1,'name':request.post['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')


def course(request):
    courses={
        'course':Course.objects.all()
        }
    return render(request,'course.html',courses)

def gallery(request):
    return render(request,'gallery.html')


def logout(request):
    return render(request,'index.html')

def login(request):
    # if request.method == "post" :
    #     email = request.post['email']
    #     password = request.post['password']
    #     try
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phno = request.POST['phno']
        password2 = request.POST['password2']
        if password == password2 :
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect ('signup')
            else:
                customer =  Staff.objects.create(email = email,name = name,password = password,phno = phno)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not match')
            return  redirect('signup')
    else:
        return render(request,'signup.html')


def forgot(request):
    return render(request,'forgot.html')

