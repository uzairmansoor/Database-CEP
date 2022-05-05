from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    hotels = Hotel_Branches.objects.all()
    context = {'hotels':hotels}
    return render(request, 'dbcep/index.html',context)

def reservation(request):
    books = Booking.objects.all()
    context1 = {'books':books}
    return render(request, 'dbcep/reservation.html',context1)


def about(request):
    return render(request,'dbcep/about.html')

def contact(request):
    return render(request,'dbcep/contact.html')

def gallery(request):
    return render(request,'dbcep/gallery.html')

def menu(request):
    return render(request,'dbcep/menu.html')