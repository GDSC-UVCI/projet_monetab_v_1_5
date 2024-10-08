from django.shortcuts import render, redirect
from school.forms.app_settings_form import AppSettingsForms


def appsetting_add(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    if request.method == 'POST':
        form = AppSettingsForms(request.POST)
        if form.is_valid():
            app_setting = form.save()
            return redirect('school:add', app_setting.id)
    else:
        form = AppSettingsForms()
    context = {
        'form': form,
    }
    return render(request, 'school/appsetting_form.html', context)

