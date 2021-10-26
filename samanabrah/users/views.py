from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    return HttpResponse("Success")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:succ")
        else:
            messages.error(request, "نام کاربری یا رمز ورود اشتباه است.")
            print("Bad Credential.")

    return render(request, "users/login.html")
