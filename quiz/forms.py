from django import forms
from .models import Question

from django import forms

class QuizForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, question in enumerate(questions):
            self.fields[f'question_{i}'] = forms.ChoiceField(
                label=question.text,
                choices=[
                    (1, question.option1),
                    (2, question.option2),
                    (3, question.option3),
                    (4, question.option4),
                ],
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                required=True
            )