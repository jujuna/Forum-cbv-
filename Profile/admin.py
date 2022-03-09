from django.contrib import admin
from .models import Category,Question,Comment,Like,DisLike

admin.site.register([Category,Question,Comment,Like,DisLike])
