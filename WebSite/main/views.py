from .forms import TaskForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': 'Main Page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def detail(request):
    return render(request, 'main/detail.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'form was not true'
    form = TaskForm()
    context = {
        'form':form,
        'error': error,
    }
    return render(request, 'main/create.html',context)

def newcreate(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/newcreate.html', context)