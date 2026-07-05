from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    data = {
        'title':'Walid\'s Portfolio',
        'name':'Munsi Walid Al Hassan Nizhu',
        'skills':['Programming', 'Algorithm', 'Python', 'PyTorch', 'TensorFlow','Datasets','NLP', 'Object Detection', 'Segmentation', 'Pose Estimation', 'FastAPI']
    }
    return render(request,"home.html",data)


def send_contact_email(request):
    if request.method != "POST":
        return redirect("/#contact")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message_body = request.POST.get("message", "").strip()

    if not name or not email or not subject or not message_body:
        messages.error(request, "Please fill in all contact fields.")
        return redirect("/#contact")

    recipient = "walidofficework@gmail.com"
    full_message = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message_body}"
    )

    email_message = EmailMessage(
        subject=f"Portfolio Contact: {subject}",
        body=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient],
        reply_to=[email],
    )
    email_message.send(fail_silently=False)

    messages.success(request, "Your message was sent.")
    return redirect("/#contact")
