from django.shortcuts import render, redirect
from .models import TodoList
from .forms import *
# Create your views here.


def index(request):
    td = TodoList.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'td': td, 'form': form}
    return render(request, 'Todo/index.html', context)


def edit(request, pk):
    etd = TodoList.objects.get(id=pk)
    form = TodoForm(instance=etd)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=etd)
        if form.is_valid():
            form.save()
        return redirect('/')

    eContext = {'etd': etd, 'form': form}
    return render(request, "Todo/edit.html", eContext)


def delete(request, pk):
    dtd = TodoList.objects.get(id=pk)
    if request.method == "POST":
        dtd.delete()
        return redirect('/')
    return render(request, "Todo/delete.html", {'dtd': dtd})


def register(request):
    return render(request, "Todo/register.html")


def login(request):
    return render(request, "Todo/login.html")
