from django.shortcuts import render
from dianapi.models import Subscriber

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Subscriber.objects.create(
            name=name,
            email=email
        )
        return render(request, "subscribe/subscribe_confirm.html", {
            "name": name
        })

    return render(request, "subscribe/subscribe_form.html")
