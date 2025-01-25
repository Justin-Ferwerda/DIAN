from rest_framework import generics
from dianapi.models import Subscriber
from dianapi.serializers import SubscriberSerializer

class SubscriberDeleteView(generics.DestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
