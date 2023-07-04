from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Subject, StudentMarks
from .forms import StudentForm, SubjectForm, StudentMarksForm
from django.contrib import messages


# Student Table CRUD operations.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Student added successfully')
            return redirect('students:student_list')
        else:
            messages.error(request,'Failed to add student, Retry!!!')
            messages.error(request,form.errors)
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated Successfully')
            return redirect('students:student_list')
        else:
            messages.error(request,'Updation Failed')
            messages.error(request,form.errors)
            
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:student_list')


# Subject Table CRUD operations

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject added successfully.')
            return redirect('students:subject_list')
        else:
            messages.error(request, ' Task Unsuccessfull. Retry!!!')
            messages.error(request, form.errors)
    else:
        form = SubjectForm()
    return render(request, 'create_subject.html', {'form': form})

def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request,'Updation Successful')
            return redirect('students:subject_list')
        else:
            messages.error(request,'Updation Failed')
            messages.error(request,form.errors)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'update_subject.html', {'form': form})

def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    subject.delete()
    return redirect('students:subject_list')


# student marks CRUD operations

def student_marks_list(request):
    student_marks = StudentMarks.objects.all()
    return render(request, 'student_marks_list.html', {'student_marks': student_marks})

def student_marks_create(request):
    if request.method == 'POST':
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks added successfully.')
            return redirect('students:student_marks_list')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            return redirect('students:student_marks_list')
    else:
        form = StudentMarksForm()
    return render(request, 'student_marks_create.html', {'form': form})

def student_marks_update(request, pk):
    student_marks = get_object_or_404(StudentMarks, pk=pk)
    if request.method == 'POST':
        form = StudentMarksForm(request.POST, instance = student_marks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks updated successfully.')
            return redirect('students:student_marks_list')
        else:
            messages.error(request,'Updation Failed')
            messages.error(request,form.errors)
    else:
        form = StudentMarksForm(instance=student_marks)
    return render(request, 'student_marks_update.html', {'form': form, 'student_marks': student_marks})

def student_marks_delete(request, pk):
    student_marks = get_object_or_404(StudentMarks, pk=pk)
    student_marks.delete()
    messages.success(request, 'Marks deleted successfully.')
    return redirect('students:student_marks_list')
    
    

def student_performance(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student_marks = StudentMarks.objects.filter(student=student)
    
    context = {
        'student': student,
        'student_marks': student_marks,
    }
    
    return render(request, 'student_performance.html', context)