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
