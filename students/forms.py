from django import forms
from .models import Student, Subject, StudentMarks

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        

class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = '__all__'