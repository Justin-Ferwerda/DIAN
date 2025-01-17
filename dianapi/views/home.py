from django.shortcuts import render

def home(request):

    return render(request, "base/index.html", {
      "subject": "I thought you might like this",
      "body": "Body"
    })
