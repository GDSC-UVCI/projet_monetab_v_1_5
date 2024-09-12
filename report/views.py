import io
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

from student.models.students_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from user.models.user_model import UserModel as User

@login_required
def index(request):
    return render(request, 'report/index.html')

@login_required
def generate_pdf(request, report_type):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, f"{report_type.capitalize()} List")

    if report_type == 'students':
        users = StudentModel.objects.all()
    elif report_type == 'teachers':
        users = TeacherModel.objects.all()
    else:
        users = User.objects.all()

    y = 700
    for user in users:
        p.drawString(100, y, f"{user.first_name}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

@login_required
def generate_excel(request, report_type):
    if report_type == 'students':
        users = StudentModel.objects.all()
    elif report_type == 'teachers':
        users = TeacherModel.objects.all()
    else:
        users = User.objects.all()

    data = [{'Pseudo': user.last_name, 'Email': user.first_na} for user in users]
    df = pd.DataFrame(data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=f"{report_type.capitalize()} List")
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@login_required
def generate_report(request):
    report_type = request.GET.get('report_type')
    report_format = request.GET.get('format')

    if report_format == 'pdf':
        return generate_pdf(request, report_type)
    elif report_format == 'excel':
        return generate_excel(request, report_type)
    else:
        return redirect('report:index')