import random
from datetime import date
from django.shortcuts import render
from django.db.models import Q
from dianapi.models import Devotion

def home(request):
    current_date = date.today()
    devotions = Devotion.objects.filter(
    Q(date__month=current_date.month) & Q(date__day=current_date.day)
    )
    devotion = random.choice(devotions)

    return render(request, "base/index.html", {
      "subject": "I thought you might like this",
      "body": "Body",
      "verse": devotion.verse,
      "content": devotion.content
    })
