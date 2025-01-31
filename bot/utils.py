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

    # Install Chrome if not found
    if not os.path.exists(chrome_path):
        print("Installing Google Chrome...")
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("apt install -y ./google-chrome-stable_current_amd64.deb")

    # Install ChromeDriver if not found
    if not os.path.exists(driver_path):
        print("Installing ChromeDriver...")
        os.system("wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip")
        os.system("unzip chromedriver_linux64.zip -d /usr/bin/")
        os.system("chmod +x /usr/bin/chromedriver")

    # Set Chrome options for headless mode
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set up ChromeDriver service
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
