from django.shortcuts import render,redirect
from .forms import EmployeeForm 
 

# Create your views here.
def addemp(request):
    context = {} 

    form = EmployeeForm(request.POST or None,request.FILES or None) 
    if form.is_valid():
        form.save()
        return redirect('/')
        
    context['form']=form

    return render(request,'add.html',context)  
    