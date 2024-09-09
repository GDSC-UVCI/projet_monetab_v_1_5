from school.models.school_model import SchoolModel
from student.models.students_model import StudentModel as Student
from teacher.models.teacher_model import TeacherModel as Teacher
from user.models.user_model import UserModel as User
def count(request):
    students=Student.objects.filter(status=True)
    schools = SchoolModel.objects.filter(status=True)
    students_female=Student.objects.filter(gender="H").count()
    students_male=Student.objects.filter(gender="M").count()
    teachers=Teacher.objects.filter(status=True)
    users=User.objects.filter(is_active=True)
    student_number=students.count()
    teacher_number=teachers.count()
    user_number=users.count()
    school_number=schools.count()
    
    return { 'total_students':student_number,
             'total_students_female':students_female,
             'total_students_male':students_male,
             'total_teachers':teacher_number,
             'total_users':user_number,
             'total_school':school_number
            }

