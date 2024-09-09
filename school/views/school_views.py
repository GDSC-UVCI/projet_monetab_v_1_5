from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from school.models.school_model import SchoolModel
from school.forms.school_form import SchoolForms
from school.forms.app_settings_form import AppSettingsForms

@login_required
def list(request):
    schools = SchoolModel.objects.filter(status=True)
    context = {
        "schools": schools,
    }
    return render(request,"school/list.html",context)

@login_required
def add_and_edit(request,pk=None):
    if pk:
        school = get_object_or_404(SchoolModel, id=pk)
    else:
        school = None

    if request.method == "POST":
        school_form = SchoolForms(request.POST, instance=school)
        app_setting_form = AppSettingsForms(request.POST, instance=school.app_setting if school else None)
        if school_form.is_valid() and app_setting_form.is_valid():
            app_setting = app_setting_form.save()
            school = school_form.save(commit=False)  
            school.app_setting = app_setting
            school.save()
            return redirect('school:list')
        
    
    school_form = SchoolForms(instance=school)
    app_setting_form = AppSettingsForms(instance=school.app_setting if school else None)
    context = {
        "form": school_form,
        'app_form':app_setting_form
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
