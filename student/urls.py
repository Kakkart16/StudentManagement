from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    # path('list/', views.student_list, name='student_list'),
    # path('subjects/', views.subject_list, name='subject_list'),
    # path('marks/', views.student_marks, name='student_marks'),
    path('list/', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
