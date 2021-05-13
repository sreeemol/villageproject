from django.shortcuts import render
from .forms import PanchayathForm,EmployeesForm,enduserForm,LeaveapplicationForm,ComplaintForm,NewsForm,SalaryForm
from .models import Panchayath,Employees,enduser,Leaveapplication,Complaint,News,Salary
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages



def index(request):
    return render(request, "index.html")

# Create your views here.
def register_panchayath(request):
    register_url = reverse('villageapp:register_panchayath')
    if request.method == 'POST':
        register_form = PanchayathForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a Panchayath entity')
            return redirect('villageapp:index')
        else:
            return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
    else:
        register_form = PanchayathForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
def register_employees(request):
    register_url = reverse('villageapp:register_employees')
    if request.method == 'POST':
        register_form = EmployeesForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a Employees entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = EmployeesForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
def register_enduser(request):
    register_url = reverse('villageapp:register_enduser')
    if request.method == 'POST':
        register_form = enduserForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a enduser entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = enduserForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
def register_Leaveapplication(request):
    register_url = reverse('villageapp:register_Leaveapplication')
    if request.method == 'POST':
        register_form = LeaveapplicationForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a Leaveapplication entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = LeaveapplicationForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )

def register_Complaint(request):
    register_url = reverse('villageapp:register_Complaint')
    if request.method == 'POST':
        register_form = ComplaintForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a Complaint entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = ComplaintForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )
def register_News(request):
    register_url = reverse('villageapp:register_News')
    if request.method == 'POST':
        register_form = NewsForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a news entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = NewsForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )

def register_Salary(request):
    register_url = reverse('villageapp:register_Salary')
    if request.method == 'POST':
        register_form = SalaryForm(data=request.POST)
        if register_form.is_valid():
            item = register_form.save()
            item.save()
            messages.success(request, 'Successfully created a salary entity')
            return redirect('villageapp:index')
        else:
            return redirect(request,
            'register.html',
            {'register_form': register_form,'register_url': register_url} )
    else:
        register_form = SalaryForm()
        return render(request,
            'register.html',
            {'register_form': register_form, 'register_url': register_url} )

    
