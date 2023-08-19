from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from dianapi.models import Devotion
from dianapi.serializers import DevotionSerializer

def devotion_view(request, devotion_id=None, is_edit=None):
    request_method = request.method

    if is_edit:
        # Not finished, Use as an example
        devotion = get_object_or_404(Devotion, pk=devotion_id)
        devotion_data = DevotionSerializer(devotion).data

        return render(request, "devotions/edit.html", {"devotion": devotion_data})

    if request_method == "GET":

        query = request.GET.get('q')

        if devotion_id:
            devotion = get_object_or_404(Devotion, pk=devotion_id)
            devotion_data = DevotionSerializer(devotion).data
            return render(request, "devotions/details.html", {"devotion": devotion_data})
        else:

            if query:
                devotions = Devotion.objects.filter(Q(verse__icontains=query))
            else:
                devotions = Devotion.objects.all()
            devotion_data = DevotionSerializer(devotions, many=True).data
            items_per_page = 25
            paginator = Paginator(devotion_data, items_per_page)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, "devotions/list.html", {'page_obj': page_obj, 'total': len(devotions), 'query': query})

    elif request_method == "POST":
        form_data = request.POST
        print(form_data["actual_method"])

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            devotion = get_object_or_404(Devotion, pk=devotion_id)
            devotion_data = DevotionSerializer(devotion).data
            return render(request, "devotions/edit.html", {"devotion": devotion_data})
        elif ("actual_method" in form_data
              and form_data["actual_method"] == "DELETE"):
            devotion = get_object_or_404(Devotion, pk=devotion_id)
            devotion_data = DevotionSerializer(devotion).data
            return render(request, "devotions/details.html", {"devotion": devotion_data})

    return render(request, "base/index.html", {})
