from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from report.models import Report


def dashboard(request):
    reports = Report.objects.filter(employee=request.user)
    return render(request, "users/dashboard.html", {"reports": reports})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:dashboard")
        else:
            messages.error(request, "نام کاربری یا رمز ورود اشتباه است.")
    # If users is already logged in go to main page
    if request.user.is_authenticated:
        return redirect("users:dashboard")
    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    return redirect("users:login")
