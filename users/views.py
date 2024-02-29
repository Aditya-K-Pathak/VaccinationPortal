from . import forms
from . import dbops
import pandas as pd
from datetime import date, datetime
from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            if dbops.Users.login(
                request.POST.get('username'), request.POST.get('password')
            ):
                return dashboard(request)
    return render(request, 'user_login.html', {'form': forms.UserLogin()})

def register(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            try:
                dbops.databaseOperations.register_user(
                    request.POST.get('username'),
                    request.POST.get('name'),
                    request.POST.get('password'),
                    request.POST.get('address'),
                    request.POST.get('email'),
                )
                return(dashboard(request))
            except KeyError:
                return HttpResponse('Username already Exists')
    return render(request, 'user_register.html', {'form': forms.UserRegister()})

def dashboard(request):
    if request.method == 'POST':
        if request.POST.get('date'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            vaccine = request.POST.get('vaccine')
            date_ = request.POST.get('date')
            code = request.POST.get('code')
            try:
                dbops.book_slot.book(
                    username, password, vaccine, date_, code
                )
                return HttpResponse('<h1>Your Slot has been booked Successfully...</h1>')
            except ValueError:
                return HttpResponse('<h1> No Slots are Available for selected day</h1>')
        else:
            credential = request.POST.get('username') + ':' + request.POST.get('password')
            data = dbops.databaseOperations.read_users_database()[credential]
            today = date.today()
            next_days = pd.date_range(today, periods=5)
            data.update(
            {
                'form': forms.SlotBooking(),
                'dates': [str(i)[:10] for i in next_days],
                'center': dbops.centerDatabaseOperations.read_centre_data()
            }
        )
    return render(request, 'user_dashboard.html', data)

def bookSlot(request):
    
    return render(request, 'book_slot.html', {})