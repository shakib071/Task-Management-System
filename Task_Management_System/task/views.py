from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import taskForm
# Create your views here.


def add_task(request):
    
    if request.method == "POST":
        task_form = taskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
        
    else:
        task_form = taskForm()
    return render(request,'add_task.html',{'form':task_form})

def edit_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task_form = taskForm(instance = task)

    if request.method == "POST":
        task_form = taskForm(request.POST,instance = task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    
    return render(request,'add_task.html',{'form':task_form})

def delete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')

def complete_task(request,id):
    task = TaskModel.objects.get(pk=id)
    task.is_Completed = True
    task.save()
    return redirect('homepage')
