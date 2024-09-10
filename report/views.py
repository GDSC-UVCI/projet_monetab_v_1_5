import io
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
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
        users = User.objects.filter(role='student')
    elif report_type == 'teachers':
        users = User.objects.filter(role='teacher')
    else:
        users = User.objects.all()

    y = 700
    for user in users:
        p.drawString(100, y, f"{user.pseudo} - {user.username}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

@login_required
def generate_excel(request, report_type):
    if report_type == 'students':
        users = User.objects.filter(role='student')
    elif report_type == 'teachers':
        users = User.objects.filter(role='teacher')
    else:
        users = User.objects.all()

    data = [{'Pseudo': user.pseudo, 'Email': user.username} for user in users]
    df = pd.DataFrame(data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=f"{report_type.capitalize()} List")
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')