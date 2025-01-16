from django.contrib import admin
from unfold.admin import ModelAdmin
from dianapi.models import Devotion

class DevotionAdmin(ModelAdmin):
    pass

admin.site.register(Devotion, DevotionAdmin)
