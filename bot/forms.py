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
    
    
# from django import forms

# class EmailForm(forms.Form):
#     emails = forms.CharField(widget=forms.Textarea, help_text="Enter one or multiple emails separated by commas.")
#     htmx_template = forms.CharField(widget=forms.Textarea, help_text="Paste your HTMX email template.")
#     subject = forms.CharField(max_length=255, initial="Dreamzz Drip Club", help_text="Enter the email subject.")


from django import forms


class EmailForm(forms.Form):
    emails = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control p-2 border rounded",
            "placeholder": "Enter emails separated by commas...",
            "rows": 3
        }),
        help_text="Enter one or multiple emails separated by commas."
    )
