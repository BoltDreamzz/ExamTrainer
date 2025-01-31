# from django.db import models

# Create your models here.
# models.py
from django.db import models

class JobWebsite(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    last_scraped = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('applied', 'Applied'), ('rejected', 'Rejected'), ('interview', 'Interview')])
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job.title} - {self.status}"
