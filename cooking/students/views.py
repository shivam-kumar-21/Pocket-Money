from django.shortcuts import render, redirect
from .models import Student, Student_Detail
from .forms import StudentDetailForm, StudentForm

# Create your views here.
def home(request):
    return render (request, 'students/home.html', {

    })

def about(request):
    return render (request, 'students/about.html', {
        'students': Student.objects.all()
    })

def student_details_list(request):
    student_details_list = Student_Detail.objects.all()
    return render(request, 'students/student_details_list.html', {
        'student_details_list': student_details_list          
    })

def student_entry(request):
    if request.method == "POST":
        student = StudentDetailForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('student_list')  # Redirect to a page showing a list of students
    else:
        student = StudentDetailForm()

    return render(request, 'students/student_info.html', { 'student' : student})