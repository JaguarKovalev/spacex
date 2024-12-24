from django.contrib import admin
from .models import Launch, UserSearch

@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin):
    list_display = ('mission_name', 'date', 'success', 'rocket')
    search_fields = ('mission_name', 'rocket')
    list_filter = ('success', 'date')


@admin.register(UserSearch)
class UserSearchAdmin(admin.ModelAdmin):
    list_display = ('user', 'search_date', 'year')
    search_fields = ('user__username',)
    list_filter = ('search_date',)
