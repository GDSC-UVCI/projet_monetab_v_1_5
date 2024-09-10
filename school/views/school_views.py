from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from school.forms.school_form import SchoolForms
from school.models.school_model import SchoolModel


@login_required
def list(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    schools = SchoolModel.objects.filter(status=True)
    context = {
        "schools": schools,
    }
    return render(request,"school/list.html",context)




def add_and_edit(request, app_setting_id=None):
    # Check if any school exists
    if SchoolModel.objects.exists():
        return redirect('dashboard:index')

    if request.method == "POST":
        school_form = SchoolForms(request.POST)
        if school_form.is_valid():
            school = school_form.save(commit=False)
            school.status = True
            if app_setting_id:
                school.app_setting_id = app_setting_id  # Use the passed AppSetting ID
            school.save()
            return redirect('login')

    school_form = SchoolForms()
    context = {
        "form": school_form,
    }
    return render(request, "school/forms.html", context)
@login_required
def delete(request,pk):
    school = get_object_or_404(SchoolModel, id=pk)
    # school.status = False
    # school.app_setting.status = False
    # school.app_setting.save()
    # school.save()
    school.delete()
    return redirect('school:list')
