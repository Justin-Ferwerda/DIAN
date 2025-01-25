from rest_framework.serializers import ModelSerializer
from dianapi.models import Subscriber

class SubscriberSerializer(ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ('id', 'name', 'email', 'mailer_lite_id')
