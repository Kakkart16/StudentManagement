from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, StudentMarks
from .forms import StudentForm

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student:student_list')

def student_list(request):
    student = Student.objects.all()
    return render(request, 'student_list.html', {'student': student})

# def subject_list(request):
#     subjects = Subject.objects.all()
#     return render(request, 'subject_list.html', {'subjects': subjects})

# def student_marks(request):
#     student_marks = StudentMarks.objects.all()
#     return render(request, 'student_marks.html', {'student_marks': student_marks})
