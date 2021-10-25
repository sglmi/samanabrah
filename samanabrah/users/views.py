from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Success")


def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("users:succ")
    else:
        print("Bad Credential.")

    return render(request, "users/login.html")
