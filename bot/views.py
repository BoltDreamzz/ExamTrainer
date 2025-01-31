# views.py
from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .utils import apply_to_job, scrape_jobs
from django.core.files.storage import FileSystemStorage

def dashboard(request):
    if request.method == "POST":
        # Handle job application
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            resume = form.FILES['resume']
            job_url = form.cleaned_data['job_url']
            job_title = form.cleaned_data['job_title']
            
            # Save the resume temporarily
            fs = FileSystemStorage()
            resume_path = fs.save(resume.name, resume)
            resume_url = fs.url(resume_path)
            
            # Apply to job with Selenium (pass dynamic user data and resume path)
            apply_to_job(job_url, full_name, email, resume_url)

            # Scrape jobs based on the URL and job title if given
            jobs = scrape_jobs(job_url, job_title)

            return render(request, 'bot/dashboard.html', {
                'form': form,
                'jobs': jobs,  # Display jobs found from scraping
                'resume_url': resume_url,
                'message': "Application submitted successfully!"
            })
    else:
        form = JobApplicationForm()

    return render(request, 'bot/dashboard.html', {
        'form': form
    })
