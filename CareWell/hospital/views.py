from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import BookingForm
from .models import Departments,Doctor,Booking

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def  booking (request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    forms= BookingForm()
    dict_form={
        'form' : forms
    }
    return render(request,'booking.html',dict_form)
def department(request):
    dict_dept={
       'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
    
def doctors(request):
    dict_docs={
        'Doctors':Doctor.objects.all()
    }
    return render( request,'doctors.html',dict_docs)
def contacts(request):
    return render(request,'contacts.html')













