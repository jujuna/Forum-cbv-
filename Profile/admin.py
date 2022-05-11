from django.contrib import admin
from .models import Category, Question, Comment, FavoriteQuestion,LikeOrDislike


admin.site.register([Category, Question, Comment, FavoriteQuestion,LikeOrDislike])

