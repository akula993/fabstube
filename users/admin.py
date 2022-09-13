from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

User = get_user_model()


# Group = get_group_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


# @admin.register(Group)
# class GroupAdmin(GroupAdmin):
#     pass
# admin.sites.register(GroupAdmin)