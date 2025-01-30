from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('select_subject/', views.select_subject, name='select_subject'),
    path('take_quiz/<int:subject_id>/', views.take_quiz, name='take_quiz'),
    path('quiz_result/<int:score_id>/', views.quiz_result, name='quiz_result'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('recommended_questions/', views.recommended_questions, name='recommended_questions'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
]
