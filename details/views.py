from multiprocessing import context
from django.shortcuts import render,redirect
from employee.models import Employee 
from addEmp.forms import EmployeeForm   
 
# Create your views here.
def detail(request,pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=emp) 
      

    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save() 
            return redirect('/employee/') 

    context = {'form':form}  

    return render(request,'details.html',context)  
    