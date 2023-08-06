from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Subscription, User


class UsersAdmin(UserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'first_name')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)


admin.site.register(User, UsersAdmin)
admin.site.register(Subscription, SubscribeAdmin)
