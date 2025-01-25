from django.core.paginator import Paginator
from django.shortcuts import render
from dianapi.models import Devotion

def devotion_list(request):
    devotions = Devotion.objects.all()
    paginator = Paginator(devotions, 5)
    page_number = request.GET.get('page')
    devotions = paginator.get_page(page_number)
    request_is_htmx = request.headers.get('HX-Request')
    template = "devotions/partial_list.html" if request_is_htmx else "devotions/list.html"
    return render(request, template, {'devotions': devotions})
