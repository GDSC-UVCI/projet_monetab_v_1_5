from django.shortcuts import render, get_object_or_404, redirect

from student.forms.absence_forms import AbsenceForm
from student.models.absence_model import AbsenceModel
from datetime import datetime
from user.forms.user_forms import UserForm
from base.forms.address_form import AddressForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def index(request):
    absences = AbsenceModel.objects.filter(status=True)
    today = datetime.now().year

    context = {
        'absences': absences,
        'today': today,
    }
    return render(request, "absence/list.html", context)



@login_required
def add_and_edit(request, pk=None):
    if pk:
        absence = get_object_or_404(AbsenceModel, id=pk)
    else:
        absence = None
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('absence:index')

    form = AbsenceForm(instance=absence)
    context = {
        'form': form,
    }
    return render(request, "absence/forms.html", context)


# def edit(request, id):
#     return render(request, "student/student_edit.html")

@login_required
def delete(request, pk):
    absence = get_object_or_404(AbsenceModel, id=pk)
    # absence.status = False
    # absence.save()
    absence.delete()
    return redirect('absence:index')
