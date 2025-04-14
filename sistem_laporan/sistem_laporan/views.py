from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect("admin_dashboard")
            else:
                return redirect("dashboard")
        else:
            messages.error(request, "Username atau password salah!")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profil(request):
    user = request.user
    return render(request, "profil.html", {"user": user})

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='dashboard')
def profil_admin(request):
    return render(request, 'profil_admin.html', {'user': request.user})
