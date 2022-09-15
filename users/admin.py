from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from users.models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ("bio", ('location', 'birth_date'), ('image', 'get_image'),)
    show_change_link = True
    readonly_fields = ('get_image', 'birth_date')

    def get_image(self, obj, ):
        return mark_safe(f'<img src={obj.image.url} width="100px height=auto">')

    get_image.short_description = "Изображение"


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [ProfileInline]
