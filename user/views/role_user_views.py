from django.shortcuts import render, redirect, get_object_or_404

from user.forms.role_user_forms import RoleUserForm
from user.models.role_model import RoleUserModel as Role
from user.models.user_model import UserModel as User

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list(request):
    roles = Role.objects.filter(status=True)
    numbers_roles = roles.count()
    context = {
        'roles': roles,
        'total': numbers_roles,
    }
    return render(request, "roleuser/list.html", context)


@login_required
def add_and_edit(request, pk=None):
    if pk:
        role = get_object_or_404(Role, id=pk)
    else:
        role = None

    if request.method == "POST":
        role_form = RoleUserForm(request.POST, instance=role)

        if role_form.is_valid():
            role_form.save()  
            return redirect('role:list')
        
    
    role_form = RoleUserForm(instance=role)
    context = {
        "form": role_form
    }
    return render(request, "roleuser/forms.html", context)

# def edit(request, id):
#   return render(request, "user/users_edit.html")

@login_required
def delete(request, pk):
    role = get_object_or_404(Role, id=pk)
    # role.status = False
    # role.save()
    # users = User.objects.filter(role=role)
    # for user in users:
    #     user.role = None
    #     user.save()
    role.delete()
    return redirect('role:list')
