import requests
import chromedriver_autoinstaller  # Auto-install correct ChromeDriver version
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Set up Chrome WebDriver with automatic driver installation."""
    chromedriver_autoinstaller.install()  # Ensure ChromeDriver is updated
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def apply_to_job(job_url, full_name, email, resume_path):
    """Uses Selenium to apply to a job by filling out forms and uploading a resume."""
    driver = setup_driver()
    driver.get(job_url)

    try:
        # Wait for the form fields to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # Locate form elements dynamically
        name_field = driver.find_element(By.NAME, "full_name")
        email_field = driver.find_element(By.NAME, "email")
        resume_field = driver.find_element(By.NAME, "resume")
        submit_button = driver.find_element(By.NAME, "submit")

        # Fill in the text fields dynamically from input
        name_field.send_keys(full_name)
        email_field.send_keys(email)
        resume_field.send_keys(resume_path)  # Upload resume
        submit_button.click()

        print(f"Successfully applied to {job_url}")

        # Wait for confirmation message or success indication
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "confirmation_message")))
    
    except Exception as e:
        print(f"Error applying to {job_url}: {e}")
    
    finally:
        driver.quit()

def scrape_jobs(website_url, job_title=None):
    """Scrapes jobs from a website. Filters jobs by title if specified."""
    response = requests.get(website_url)
    jobs = [
        {'title': 'Python Developer', 'company': 'Company A', 'location': 'Remote', 'link': 'https://www.linkedin.com'},
    ]  # Placeholder data
    
    if job_title:
        jobs = [job for job in jobs if job_title.lower() in job['title'].lower()]
    
    return jobs
