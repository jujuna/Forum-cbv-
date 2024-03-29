from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','mobile')
    list_display_links = ('email','username')


admin.site.register(User,UserAdmin)
