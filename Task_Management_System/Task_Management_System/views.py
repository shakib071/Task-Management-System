from django.shortcuts import render
from task.models import TaskModel

def home(request):
    all_tasks = TaskModel.objects.all()

    return render(request,'home.html',{'tasks': all_tasks})
    