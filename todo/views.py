from django.shortcuts import render, redirect
from .models import TodoList
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import *
# Create your views here.


def index(request):
    td = TodoList.objects.all()
    form = TodoForm()
    if request.method == "POST":
        # data = request.POST['work']
        specify = TodoList(user=request.user)
        form = TodoForm(request.POST)
        if form.is_valid():
            specify.save()
            form.save()

            # new = TodoList(content=form, user=request.user)
        return redirect("/home")

    context = {'td': td, 'form': form, }
    return render(request, 'Todo/index.html', context)


def edit(request, pk):
    etd = TodoList.objects.get(id=pk)
    form = TodoForm(instance=etd)
    if request.method == 'POST':
        specify = TodoList(user=request.user)
        form = TodoForm(request.POST, instance=etd)
        if form.is_valid():
            specify.save()
            form.save()
        return redirect('/home')

    eContext = {'etd': etd, 'form': form, }
    return render(request, "Todo/edit.html", eContext)


def delete(request, pk):
    dtd = TodoList.objects.get(id=pk)
    if request.method == "POST":
        dtd.delete()
        return redirect('/home')
    return render(request, "Todo/delete.html", {'dtd': dtd})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return redirect("/reg")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email taken")
                return redirect("/reg")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Successfully registered")
                return redirect("/")
        else:
            messages.error(request, "Password didn't match")
            return redirect("/reg")

        messages.success(request, "Successfully registered")
        return redirect("/")
    else:
        return render(request, "Todo/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "successfully loged in")
            return redirect("/home")
        else:
            messages.error(request, "Invalid cridential")
            return redirect("/")
    else:
        messages.error(request, "Invalid cridential")
        return render(request, "Todo/login.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "Loged out from the site")
    return redirect("/")
