from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    # subjects = models.ManyToManyField('Subject', through='StudentMarks')

    def __str__(self):
        return str(self.student_id) + "-" + self.name


class Subject(models.Model):
    subject_id = models.CharField(max_length=4, primary_key=True)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_id + " - " + self.subject_name

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    class Meta:
        unique_together = ('student', 'subject')
    
    def __str__(self):
        return f"{str(self.student.student_id)} - {self.subject.subject_id}: {self.marks}"


