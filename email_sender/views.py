from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def email_sender(request):

    context = {}
    if request.method == "POST":
        subj = request.POST.get("subject")
        msg = request.POST.get("message")
        address = request.POST.get("address")

        if address and subj and msg:
            try:
                send_mail(subj, msg, settings.EMAIL_HOST_USER, [address])
                context["result"] = "Email sent sucssfully!!!!"
            except Exception as e:
                context["result"] = f"Error sending email: {e}"
        else:
            context["result"] = "All fields are required"

    return render(request, "email_sender.html", context)
