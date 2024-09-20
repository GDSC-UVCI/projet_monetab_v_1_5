from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404

from user.forms.user_forms import UserForm
from user.models.user_model import UserModel
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    users = UserModel.objects.all()
    numbers_users = users.count()
    context = {
        'users': users,
        'total': numbers_users,
    }
    return render(request, "user/list.html", context)


@login_required
def add_and_edit(request, pk=None):
    if pk:
        user = get_object_or_404(UserModel, id=pk)
    else:
        user = None

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            print('success')
            user = user_form.save(commit=False)
            if request.POST.get('password'):
                user.password = make_password(request.POST['password'])
            user.save()
            return redirect('user:index')
        else:
            return render(request, 'user/forms.html', {"form": user_form})

    user_form = UserForm(instance=user)
    context = {
        "form": user_form
    }
    return render(request, "user/forms.html", context)



@login_required
def change_user_status(request, pk, action):
    user = get_object_or_404(User, id=pk)
    if action == 'activate':
        user.is_active = True
    elif action == 'deactivate':
        user.is_active = False
    user.save()
    return redirect('user:index')


@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(pseudo__icontains=query) | Q(email__icontains=query))
    else:
        users = User.objects.all()
    numbers_users = users.count()
    context = {
        'users': users,
        'total': numbers_users,
        'query': query,
    }
    return render(request, "user/list.html", context)