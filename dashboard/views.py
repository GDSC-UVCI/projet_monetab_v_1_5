from django.shortcuts import render, redirect
from user.forms.user_forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from base.management.create_default_user import CreateDefaultUser

# Create your views here.
@login_required
def index(request):
    return render(request, "dashboard/index.html")


def log_in(request):
    next_url = request.GET.get('next', '')
    print(next_url)
    CreateDefaultUser().create_default_user("admin", "admin")
    print(request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
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
    return redirect('')
