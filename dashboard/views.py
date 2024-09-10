from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from school.models.app_setting_model import AppSettingModel
from school.models.school_model import SchoolModel
from user.forms.user_forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from base.management.create_default_user import CreateDefaultUser


# Create your views here.
def check_initial_setup(request):
    # Check if the admin user exists
    if not User.objects.filter(username='admin').exists():
        # Create a superuser with default credentials
        User.objects.create_superuser(username='admin', password='admin', email='')

    # Check if AppSetting exists
    if not AppSettingModel.objects.exists():
        return redirect('appsetting_add')  # Redirect to AppSetting add page

    # Get the AppSetting instance
    app_setting = AppSettingModel.objects.first()

    # Check if School exists
    if not SchoolModel.objects.exists():
        return redirect('school:add', app_setting_id=app_setting.id)  # Pass AppSetting ID to the add view

    # If all checks pass, redirect to login
    return redirect('login')

@login_required
def index(request):
    if not AppSettingModel.objects.exists() or not SchoolModel.objects.exists():
        return redirect('dashboard:check_initial_setup')
    return render(request, "dashboard/index.html")



def log_in(request):
    if not AppSettingModel.objects.exists() or not SchoolModel.objects.exists():
        return redirect('dashboard:check_initial_setup')

    next_url = request.GET.get('next', 'login')


    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            # Try to authenticate using Django's default backend
            user = authenticate(request, username=username, password=password)
            if user is None:
                # If authentication with Django's backend fails, try the custom backend
                user = authenticate(request, username=username, password=password, backend='user.backends.CustomUserModelBackend')
            if user is not None:
                login(request, user)
                return redirect(next_url)
            messages.error(request, "Veuillez entrer un username ou un mot de passe valide")
        else:
            messages.error(request, "Veuillez entrer un username et un mot de passe")

    form = UserForm()
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    context = {
        'form': form
    }
    return render(request, "login.html", context)

def log_out(request):
    logout(request)
    return redirect('login')
