from django.contrib import admin
from .models import Category,Question,Comment

admin.site.register([Category,Question,Comment])
