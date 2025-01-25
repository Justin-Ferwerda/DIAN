from django.db import IntegrityError
from django.shortcuts import render
from dianapi.models import Subscriber
from utils import MailerLiteService

def subscribe(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        try:
            subscriber = Subscriber.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            name = first_name + ' ' + last_name
            mailer = MailerLiteService()
            mailer_lite_subscriber_object = mailer.create_subscriber(email, name)
            subscriber.mailer_lite_id = mailer_lite_subscriber_object["data"]["id"]
            subscriber.save()

            return render(request, "subscribe/subscribe_confirm.html", {
                "name": name
            })

        except IntegrityError:
            error = "Looks like you're already subscribed! Would you like to enter a different email?"
            return render(request, "subscribe/subscribe_form.html", {
                "error": error
            })

    return render(request, "subscribe/subscribe_form.html")
