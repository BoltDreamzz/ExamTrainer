# Step 1: Use an official Python runtime as a parent image
FROM python:3.12

# Step 2: Set the working directory inside the container
WORKDIR /examtrainer

# Step 3: Copy the current directory contents into the container
COPY . /examtrainer

# Step 4: Install system dependencies and Google Chrome
RUN apt-get update && apt-get install -y wget unzip \
    # Install dependencies for Chrome and Selenium
    && apt-get install -y curl gnupg2 ca-certificates \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Step 5: Install ChromeDriver (match the installed Chrome version)
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d'.' -f1) && \
    wget -q "https://chromedriver.storage.googleapis.com/${CHROME_VERSION}.0.5735.90/chromedriver_linux64.zip" -O chromedriver.zip && \
    unzip chromedriver.zip -d /usr/bin/ && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver.zip

# Step 6: Install any needed Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Migrate the database and collect static files
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput --clear

# Step 8: Expose port 8000 for the web service
EXPOSE 8000

# Step 9: Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=examtrainer.settings

# Step 10: Command to run the web application using gunicorn
CMD ["gunicorn", "examtrainer.wsgi:application", "--bind", "0.0.0.0:8000"]
