from rest_framework.serializers import ModelSerializer
from dianapi.models import Devotion

class DevotionSerializer(ModelSerializer):

    class Meta:
      
        model = Devotion
        fields = ('id', 'date', 'verse', 'content')
