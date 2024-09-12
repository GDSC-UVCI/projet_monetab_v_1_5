from django.shortcuts import render, get_object_or_404, redirect

from student.forms.students_cards_forms import StudentCardForm
from student.models.students_cards_model import StudentsCardsModel
from datetime import datetime
from user.forms.user_forms import UserForm
from base.forms.address_form import AddressForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def index(request):
    students_cards = StudentsCardsModel.objects.filter(status=True)
    today = datetime.now().year
    total = students_cards.count()

    context = {
        'students_cards': students_cards,
        'today': today,
        'total': total
    }
    return render(request, "students_cards/list.html", context)



@login_required
def add_and_edit(request, pk=None):
    if pk:
        student_cards = get_object_or_404(StudentsCardsModel, id=pk)
    else:
        student_cards = None
    if request.method == 'POST':
        form = StudentCardForm(request.POST, instance=student_cards)
        if form.is_valid():
            form.save()
            return redirect('studentcards:index')

    form = StudentCardForm(instance=student_cards)
    context = {
        'form': form,
    }
    return render(request, "students_cards/forms.html", context)


# def edit(request, id):
#     return render(request, "student/student_edit.html")

@login_required
def delete(request, pk):
    student_cards = get_object_or_404(StudentsCardsModel, id=pk)
    # student_cards.status = False
    # student_cards.save()
    student_cards.delete()
    return redirect('studentcards:index')
