from django.contrib import admin
from django.utils.safestring import mark_safe
from tube.models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('file',)}
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'profile.user', None) is None:
            obj.profile = request.user
        obj.save()