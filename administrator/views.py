from django.shortcuts import render, HttpResponse
from . import forms
from . import dbops

# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST.get('code'):
            dbops.VaccinationCenter.delete_center(request.POST.get('code'))
            return HttpResponse(
                f'<h1>Center {request.POST.get("code")} is now permanently deleted! </h1><a href="./">Go to Dashboard </a>'
            )
        if request.POST.get('username'):
            admins = dbops.databaseOperations.read_admin_data()
            if request.POST.get('username') in admins and request.POST.get('password') == admins[request.POST.get('username')]:
                return render(request, 'dashboard.html', {
                    'data': dbops.VaccinationCenter.get_all_centers(),
                    'form': forms.DeleteCenter()
                })
    return render(request, 'index.html', {'form': forms.loginForm()})

def edit(request):
    if request.method == 'POST':
        if request.POST.get('centerCode'):
            try:
                dbops.VaccinationCenter.update_center(
                    request.POST.get('centerCode'),
                    request.POST.get('centerName'),
                    request.POST.get('centerLocation'),
                    request.POST.get('vaccineName'),
                    request.POST.get('availableDoseCount'),
                    request.POST.get('openingTime'),
                    request.POST.get('closingTime'),
                )
            except ValueError:
                return HttpResponse('Center Does Not Exist')
            
    return render(request, 'admin_edit.html', {'form': forms.CenterEdit()})