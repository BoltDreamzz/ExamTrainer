import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess

def setup_driver():
    """Setup Chrome WebDriver for Selenium"""
    chrome_path = "/usr/bin/google-chrome"
    driver_path = "/usr/bin/chromedriver"

    if not os.path.exists(chrome_path):
        raise FileNotFoundError("Google Chrome not found. Ensure it's installed.")

    if not os.path.exists(driver_path):
        raise FileNotFoundError("ChromeDriver not found. Ensure it's installed.")

    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def apply_to_job(job_url, full_name, email, resume_path):
    """Uses Selenium to apply to a job by filling out forms and uploading a resume."""
    driver = setup_driver()
    driver.get(job_url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "full_name")))

        # Fill out the form dynamically
        name_field = driver.find_element(By.NAME, "full_name")
        email_field = driver.find_element(By.NAME, "email")
        resume_field = driver.find_element(By.NAME, "resume")

        name_field.send_keys(full_name)
        email_field.send_keys(email)
        resume_field.send_keys(resume_path)

        # Submit the form
        submit_button = driver.find_element(By.NAME, "submit")
        submit_button.click()

        print(f"Successfully applied to {job_url}")

        # Wait for confirmation
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "confirmation_message")))

    except Exception as e:
        print(f"Error applying to {job_url}: {e}")

    driver.quit()
