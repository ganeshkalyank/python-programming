from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.order_by("title")
    context = {"tasks": tasks}
    return render(request, "myapp/index.html", context)


def add(request):
    task = Task(title=request.POST["title"],description=request.POST["description"])
    task.save()
    return redirect(index)


def delete(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect(index)

def edit(request, task_id):
    if request.method == "POST":
        tasktoedit = Task.objects.get(id=task_id)
        tasktoedit.title = request.POST["title"]
        tasktoedit.description = request.POST["description"]
        tasktoedit.save()
        return redirect(index)
    else:
        tasktoedit = Task.objects.get(id=task_id)
        context = {"task": tasktoedit}
        return render(request, "myapp/edit.html", context)
