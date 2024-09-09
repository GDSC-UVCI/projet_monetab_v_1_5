from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from teacher.forms.teacher_forms import TeacherForm
from teacher.models.teacher_model import TeacherModel
from user.forms.user_forms import UserForm
from base.forms.adress_form import AdressForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    teachers = TeacherModel.objects.filter(status=True)
    today = datetime.now().year
    numbers_teacher = teachers.count()
    context = {
        'teachers': teachers,
        'total': numbers_teacher,
        'today': today,
    }
    return render(request, "teacher/list.html", context)


@login_required
def add_and_edit(request, pk=None):
    teacher = get_object_or_404(TeacherModel, id=pk) if pk else None

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=teacher.user if teacher else None)
        adress_form = AdressForm(request.POST, instance=teacher.adress if teacher else None)
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid() and user_form.is_valid() and adress_form.is_valid():
            user = user_form.save()
            adress = adress_form.save()
            teacher = form.save(commit=False)
            teacher.user= user
            teacher.adress = adress
            teacher.save()

            return redirect('teacher:index')
    else:
        form = TeacherForm(instance=teacher)
        user_form = UserForm(instance=teacher.user if teacher else None)
        adress_form = AdressForm(instance=teacher.adress if teacher else None)

    context = {
        'form': form,
        'user_form': user_form,
        'adress_form': adress_form
    }
    return render(request, "teacher/forms.html", context)




# def edit(request, pk):
#     pass

@login_required
def delete(request, pk):
    teacher = get_object_or_404(TeacherModel, id=pk)
    # teacher.status = False
    # teacher.user.is_active = False
    # teacher.user.save()
    # teacher.save()
    teacher.delete()
    return redirect('teacher:index')
