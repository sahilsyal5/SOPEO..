from django.shortcuts import render
from employee.models import Employee 
 

# Create your views here.
def emp(request):
    data = Employee.objects.all()
    return render(request,'employee.html',{
        'data':data
    })  
    