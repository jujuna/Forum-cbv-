from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User=get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("სახელი"))

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("კითხვა"))
    category = models.ManyToManyField(Category, related_name="categories",verbose_name=_("კატეგორია"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("მომხმარებელი"))

    def __str__(self):
        return self.title


