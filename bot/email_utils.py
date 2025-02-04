from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_marketing_email(emails, context_data, subject="Dreamzz Drip Club"):
    """
    Function to send a marketing email using a predefined Django template.

    Args:
        emails (list): A list of recipient emails.
        context_data (dict): Context data to pass into the template.
        subject (str): Subject of the email (default: 'Dreamzz Drip Club').

    Returns:
        None
    """

    if isinstance(emails, str):
        emails = [email.strip() for email in emails.split(",")]  # Convert single email to list

    # Render the email template with context
    html_content = render_to_string("emails/marketing_email.html", context_data)

    # Create email message
    email = EmailMultiAlternatives(
        subject=subject,
        body="Your email client does not support HTML emails.",  # Fallback for plain text clients
        from_email=settings.DEFAULT_FROM_EMAIL,  # Ensure you set this in settings.py
        to=emails,
    )
    email.attach_alternative(html_content, "text/html")  # Attach HTML version

    # Send the email
    email.send()
