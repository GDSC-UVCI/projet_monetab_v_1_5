from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from school.models.app_setting_model import AppSettingModel
from school.models.school_model import SchoolModel
from user.forms.user_forms import UserForm

@login_required
def index(request):
    if not AppSettingModel.objects.exists() or not SchoolModel.objects.exists():
        return redirect('appsetting_add')
    return render(request, "dashboard/index.html")

def log_in(request):
    if not AppSettingModel.objects.exists() or not SchoolModel.objects.exists():
        return redirect('appsetting_add')

    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            user = authenticate(request, username=username, password=password, backend='user.backends.CustomUserModelBackend')
        if user:
            login(request, user)
            return redirect('dashboard:index')
        messages.error(request, "Veuillez entrer un username ou un mot de passe valide")
    else:
        messages.error(request, "Veuillez entrer un username et un mot de passe")

    form = UserForm()
    return render(request, "login.html", {'form': form})

def log_out(request):
    logout(request)
    return redirect('login')