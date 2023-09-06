from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})
