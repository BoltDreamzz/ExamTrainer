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
            
from django import forms
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered'})
    )
    password2 = forms.CharField(
        label="Confirm Password", 
        widget=forms.PasswordInput(attrs={'class': 'input input-bordered'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered'}),
        }

    def clean_password2(self):
        """Check if both passwords match."""
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2