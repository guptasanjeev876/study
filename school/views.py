from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):

    #student = Teacher.objects.filter(id = 12).update(epnum = "6")
    student = Student.objects.all()
    #student = Student.objects.all()

    #qs1 = Student.objects.values_list('id', 'name', 'city', named = True)
    #qs2 = Student.objects.values_list('id', 'name', 'city', named = True)
    #student = qs2.intersection(qs1
    return render(request, 'school/home.html', {'students': student})

def teacher_data(request):
    teach = Teacher.objects.all()
    return render(request, 'school/Teacher.html', {'teacher': teach})