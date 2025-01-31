# utils.py
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def apply_to_job(job_url, full_name, email, resume_path):
    """Uses Selenium to apply to a job by filling out forms and uploading a resume."""
    # Set up ChromeDriver with Selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(job_url)

    try:
        # Wait for the form fields to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "full_name")))

        # Fill out the form with dynamic user data
        name_field = driver.find_element(By.NAME, "full_name")
        email_field = driver.find_element(By.NAME, "email")
        resume_field = driver.find_element(By.NAME, "resume")

        # Fill in the text fields dynamically from input
        name_field.send_keys(full_name)
        email_field.send_keys(email)

        # Upload the resume by sending the file path to the file input field
        resume_field.send_keys(resume_path)

        # Submit the form (adjust the selector as needed for the submit button)
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()

        print(f"Successfully applied to {job_url}")

        # Wait for confirmation message or any indication of success
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "confirmation_message")))

    except Exception as e:
        print(f"Error applying to {job_url}: {e}")
    
    # Close the driver after submission
    driver.quit()

def scrape_jobs(website_url, job_title=None):
    """Scrapes jobs from a website. Filters jobs by title if specified."""
    response = requests.get(website_url)
    jobs = []

    # Example: Simulated job data. Replace this with actual scraping logic.
    jobs = [
        {'title': 'Python Developer', 'company': 'Company A', 'location': 'Remote', 'link': 'https://https://www.linkedin.com'},
        # {'title': 'Java Developer', 'company': 'Company B', 'location': 'On-site', 'link': 'https://example.com/job2'}
    ]
    
    if job_title:
        jobs = [job for job in jobs if job_title.lower() in job['title'].lower()]

    return jobs
