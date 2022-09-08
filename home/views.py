from django.shortcuts import render
from employee.models import Employee

# Create your views here.
def index(request):  

    #counting number of employees
    empNumber = Employee.objects.count()  
    
    #data's used for chart 
    all_emp = Employee.objects.all() 

    active = [] 
    leave = [] 
    on_leave = [] 

    for emp in all_emp:
        if emp.State == 'Active':
            toAdd = '{} - {} {} |'.format(emp.id,emp.Name,emp.Surname)
            active.append(toAdd)
        if emp.State == 'Leave_count':
            toAdd = '{} - {} {} |'.format(emp.id,emp.Name,emp.Surname)
            leave.append(toAdd)
        if emp.State == 'On_leave':
            toAdd = '{} - {} {} |'.format(emp.id,emp.Name,emp.Surname)
            on_leave.append(toAdd)


    return render(request,'home.html',{
        'no':empNumber ,
        'active':active,
        'leave':leave, 
        'on_leave':on_leave
        })