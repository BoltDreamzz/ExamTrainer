from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Question, Score
from .forms import QuizForm
import random

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/index.html', {
        'subjects': subjects
    })


@login_required
def select_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz/select_subject.html', {'subjects': subjects})

# @login_required
# def take_quiz(request, subject_id):
#     subject = Subject.objects.get(id=subject_id)
#     questions = list(Question.objects.filter(subject=subject).order_by('?')[:50])

#     if request.method == "POST":
#         form = QuizForm(questions, request.POST)
#         if form.is_valid():
#             correct = 0
#             for i, question in enumerate(questions):
#                 user_answer = int(form.cleaned_data[f'question_{i}'])
#                 if user_answer == question.correct_option:
#                     correct += 1

#             score = Score.objects.create(user=request.user, subject=subject, score=correct)
#             return redirect('quiz:quiz_result', score_id=score.id)

#     else:
#         form = QuizForm(questions)

#     return render(request, 'quiz/take_quiz.html', {'form': form, 'subject': subject})

@login_required
def take_quiz(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    questions = list(Question.objects.filter(subject=subject).order_by('?')[:50])
    count = len(questions)
    
    # if count == 0:
    #     return redirect('quiz:coming_soon')

    if request.method == "POST":
        form = QuizForm(questions, request.POST)
        if form.is_valid():
            correct = 0
            easy_correct = 0
            medium_correct = 0
            hard_correct = 0
            
            for i, question in enumerate(questions):
                user_answer = int(form.cleaned_data[f'question_{i}'])
                if user_answer == question.correct_option:
                    correct += 1
                    if question.difficulty == "easy":
                        easy_correct += 1
                    elif question.difficulty == "medium":
                        medium_correct += 1
                    else:
                        hard_correct += 1

            score = Score.objects.create(
                user=request.user, 
                subject=subject, 
                score=correct,
                easy_correct=easy_correct,
                medium_correct=medium_correct,
                hard_correct=hard_correct
            )
            return redirect('quiz:quiz_result', score_id=score.id)

    else:
        form = QuizForm(questions)

    return render(request, 'quiz/take_quiz.html', {'form': form, 'subject': subject, 'count': count})

@login_required
def quiz_result(request, score_id):
    score = Score.objects.get(id=score_id)
    return render(request, 'quiz/quiz_result.html', {'score': score})


@login_required
def user_dashboard(request):
    scores = Score.objects.filter(user=request.user).order_by('-date')
    return render(request, 'quiz/dashboard.html', {'scores': scores})

@login_required
def recommended_questions(request):
    user_scores = Score.objects.filter(user=request.user)
    
    weak_subjects = user_scores.order_by('score')[:2]  # Get 2 weakest subjects
    recommended_questions = []
    
    for score in weak_subjects:
        recommended_questions.extend(list(Question.objects.filter(subject=score.subject).order_by('?')[:10]))

    return render(request, 'quiz/recommended_questions.html', {'questions': recommended_questions})

def coming_soon(request):
    return render(request, 'quiz/coming_soon.html')