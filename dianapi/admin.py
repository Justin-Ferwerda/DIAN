from django.contrib import admin
from unfold.admin import ModelAdmin
from dianapi.models import Devotion, Subscriber

class SubscriberAdmin(ModelAdmin):
    pass

class DevotionAdmin(ModelAdmin):
    ordering = ('-date',)

admin.site.register(Devotion, DevotionAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
