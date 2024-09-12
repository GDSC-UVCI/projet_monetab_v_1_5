from django.shortcuts import render, get_object_or_404, redirect

from student.forms.students_forms import StudentForm
from student.models.students_model import StudentModel
from datetime import datetime
from user.forms.user_forms import UserForm
from base.forms.address_form import AddressForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def index(request):
    students = StudentModel.objects.filter(status=True)
    today = datetime.now().year

    context = {
        'students': students,
        'today': today,
    }
    return render(request, "student/list.html", context)



@login_required
def add_and_edit(request, pk=None):
    if pk:
        student = get_object_or_404(StudentModel, id=pk)
    else:
        student = None
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=student.user if student else None)
        address_form = AddressForm(request.POST, instance=student.address if student else None)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid() and user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            address = address_form.save()
            student = form.save(commit=False)
            student.user = user
            student.address = address
            student.save()
            print('success')
            return redirect('student:index')

    form = StudentForm(instance=student)
    user_form = UserForm(instance=student.user if student else None)
    address_form = AddressForm(instance=student.address if student else None)
    context = {
        'form': form,
        'user_form': user_form,
        'address_form': address_form,
    }
    return render(request, "student/forms.html", context)


# def edit(request, id):
#     return render(request, "student/student_edit.html")

@login_required
def delete(request, pk):
    student = get_object_or_404(StudentModel, id=pk)
    # student.status = False
    # student.user.is_active = False
    # student.user.save()
    # student.save()
    student.delete()
    return redirect('student:index')
