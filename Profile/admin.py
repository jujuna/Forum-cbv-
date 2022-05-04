from django.contrib import admin
from .models import Category, Question, Comment, Like, DisLike, FavoriteQuestion


class LikeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form,  change):
        print("შემოვიდაააააააააააააააა")
        obj.decrease = True
        return super(LikeAdmin,self).save_model(request, obj, form, change)


admin.site.register([Category, Question, Comment, DisLike, FavoriteQuestion])

admin.site.register(Like, LikeAdmin)
