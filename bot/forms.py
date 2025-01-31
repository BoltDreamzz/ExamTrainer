from django import forms

class JobApplicationForm(forms.Form):
    full_name = forms.CharField(
        max_length=255, 
        label="Full Name", 
        widget=forms.TextInput(attrs={'class': 'input input-bordered'})
    )
    email = forms.EmailField(
        label="Email Address", 
        widget=forms.EmailInput(attrs={'class': 'input input-bordered'})
    )
    resume = forms.FileField(
        label="Upload Resume", 
        widget=forms.ClearableFileInput(attrs={'class': 'file-input file-input-bordered'})
    )
    job_url = forms.URLField(
        label="Job Website URL", 
        widget=forms.URLInput(attrs={'class': 'input input-bordered'})
    )
    job_title = forms.CharField(
        max_length=255, 
        required=False, 
        label="Job Title (optional)", 
        widget=forms.TextInput(attrs={'class': 'input input-bordered'})
    )