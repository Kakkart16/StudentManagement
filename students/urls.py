from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    
    path('list/', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.create_subject, name='create_subject'),
    path('subjects/update/<str:subject_id>/', views.update_subject, name='update_subject'),
    path('subjects/delete/<str:subject_id>/', views.delete_subject, name='delete_subject'),
    
    path('student-marks/', views.student_marks_list, name='student_marks_list'),
    path('student-marks/create/', views.student_marks_create, name='student_marks_create'),
    path('student-marks/update/<int:pk>/', views.student_marks_update, name='student_marks_update'),
    path('student-marks/delete/<int:pk>/', views.student_marks_delete, name='student_marks_delete'),
    
    path('<int:student_id>/performance/', views.student_performance, name='student_performance'),

]
