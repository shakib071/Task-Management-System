from django.shortcuts import render,redirect

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