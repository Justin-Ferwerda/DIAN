from django.db import IntegrityError
from django.shortcuts import render
from dianapi.models import Subscriber

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        try:
            Subscriber.objects.create(
                name=name,
                email=email
            )
            return render(request, "subscribe/subscribe_confirm.html", {
                "name": name
            })
        except IntegrityError:
            error = "Looks like you're already subscribed! Would you like to enter a different email?"
            return render(request, "subscribe/subscribe_form.html", {
                "error": error
            })

    return render(request, "subscribe/subscribe_form.html")
