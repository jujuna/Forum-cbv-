from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse

User=get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("სახელი"))

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("სათაური"))
    text = models.TextField(verbose_name=_('კითხვა'))
    category = models.ManyToManyField(Category, related_name="categories",verbose_name=_("კატეგორია"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("მომხმარებელი"))

    def get_absolute_url(self):
        return reverse('Profile:question-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField( verbose_name=_("კომენტარი"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("მომხმარებელი"))
    question = models.ForeignKey(Question,on_delete=models.CASCADE, verbose_name=_("კითხვა"))
    time = models.DateTimeField(auto_now_add=True,editable=False)
