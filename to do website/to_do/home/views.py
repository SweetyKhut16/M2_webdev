from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login, logout, authenticate
from .models import  Contact_us, Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForms
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def home(request):
    # data = Skills.objects.all()
    # context = {"skills": data}
    return render(request, 'index.html')   
    
@login_required(login_url='loginpage')
def task(request):
    data = Task.objects.all()
    context = {"tasks": data}
    return render(request, 'task.html',context)  

def newtaskAdd(request):
    form = TaskForms()
    if request.method == 'POST':
        Data = TaskForms(request.POST)
        if Data.is_valid():
            Data.save()
            messages.success(request, 'Task Added Successfully!')
            return redirect('task')
    context = {"form":form}
    return render(request, 'newtaskAdd.html', context)

def taskDelete(request,pk):
    data = Task.objects.get(id=pk)
    messages.warning(request,'Task deleted successfully')
    data.delete()
    return redirect('task')

def taskUpdate(request,pk):
    myData = Task.objects.get(id=pk)
    updateForm = TaskForms(request.POST or None ,instance=myData)
    
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request,'Task updated successfully')
        return redirect('task')
    
    context = {"form":updateForm}
    return render(request, 'updatetask.html',context)

def loginpage(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("error 404: credentials not found")
            return redirect('loginpage')
    return render(request, 'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('home')