from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Task

# Create your views here.
    
def task(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request,'task/task_list.html', context)

def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print(task)
    return render(request,'task/task_list.html')