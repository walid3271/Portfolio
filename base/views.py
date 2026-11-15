import logging
import re
from datetime import date, timedelta

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from . import data

logger = logging.getLogger(__name__)

CONTACT_RECIPIENT = "walidofficework@gmail.com"
MAX_LEN = {"name": 100, "email": 254, "subject": 150, "message": 5000}
RATE_LIMIT = 5          # messages ...
RATE_WINDOW = 60 * 60   # ... per hour per IP (best effort on serverless)


def _contact_redirect():
    return redirect(f"{reverse('home')}#contact")


def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    return forwarded.split(",")[0].strip() or request.META.get("REMOTE_ADDR", "")


CAREER_START = date(2024, 2, 1)  # first AI role (HawkEyes internship)


def experience_duration(today=None):
    """Return (years, months, days) of professional experience up to today."""
    today = today or date.today()
    years = today.year - CAREER_START.year
    months = today.month - CAREER_START.month
    days = today.day - CAREER_START.day
    if days < 0:
        # borrow the length of the previous month
        prev_month_end = today.replace(day=1) - timedelta(days=1)
        days += prev_month_end.day
        months -= 1
    if months < 0:
        months += 12
        years -= 1
    return max(years, 0), max(months, 0), max(days, 0) if years >= 0 else 0


def home(request):
    years, months, days = experience_duration()
    context = {
        "name": "Munsi Walid Al Hassan Nizhu",
        "social_links": data.SOCIAL_LINKS,
        "experience": data.EXPERIENCE,
        "education": data.EDUCATION,
        "skills": data.SKILLS,
        "projects": data.PROJECTS,
        "year": date.today().year,
        "exp_years": years,
        "exp_months": months,
        "exp_days": days,
    }
    return render(request, "home.html", context)


@require_POST
def send_contact_email(request):
    # Honeypot: real users never fill this hidden field.
    if request.POST.get("website", ""):
        return _contact_redirect()

    fields = {k: request.POST.get(k, "").strip() for k in MAX_LEN}

    if not all(fields.values()):
        messages.error(request, "Please fill in all contact fields.")
        return _contact_redirect()

    if any(len(fields[k]) > MAX_LEN[k] for k in MAX_LEN):
        messages.error(request, "One of the fields is too long.")
        return _contact_redirect()

    try:
        validate_email(fields["email"])
    except ValidationError:
        messages.error(request, "Please enter a valid email address.")
        return _contact_redirect()

    # Prevent header injection through single-line fields.
    if re.search(r"[\r\n]", fields["name"] + fields["subject"] + fields["email"]):
        messages.error(request, "Invalid characters in the form.")
        return _contact_redirect()

    key = f"contact:{_client_ip(request)}"
    count = cache.get(key, 0)
    if count >= RATE_LIMIT:
        messages.error(request, "Too many messages. Please try again later.")
        return _contact_redirect()
    cache.set(key, count + 1, RATE_WINDOW)

    body = (
        f"Name: {fields['name']}\n"
        f"Email: {fields['email']}\n"
        f"Subject: {fields['subject']}\n\n"
        f"Message:\n{fields['message']}"
    )
    email_message = EmailMessage(
        subject=f"Portfolio Contact: {fields['subject']}",
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[CONTACT_RECIPIENT],
        reply_to=[fields["email"]],
    )
    try:
        email_message.send(fail_silently=False)
    except Exception:
        logger.exception("Contact email failed to send")
        messages.error(request, "Sorry, your message could not be sent. Please email me directly.")
        return _contact_redirect()

    messages.success(request, "Your message was sent. Thank you!")
    return _contact_redirect()


def page_not_found(request, exception):
    return render(request, "404.html", status=404)
