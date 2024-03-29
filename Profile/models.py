import time

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import pre_delete,post_delete
from django.dispatch import receiver

User = get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("სახელი"))

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("სათაური"))
    text = models.TextField(verbose_name=_('კითხვა'))
    category = models.ManyToManyField(Category, related_name="categories",verbose_name=_("კატეგორია"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("მომხმარებელი"),related_name="user")
    added_time = models.DateTimeField(auto_now_add=True)
    # added_time.editable = True
    can_update = models.IntegerField(default=2)

    def question_update_limit(self):
        self.can_update -= 1
        self.save()
        return self.can_update

    def update_access(self):
        result = False if self.can_update == 0 else True
        return result

    def get_absolute_url(self):
        return reverse('Profile:question-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class LikeOrDislike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("კითხვა"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("მომხმარებელი"))
    like_dislike = models.BooleanField()

    def __str__(self):
        return str(self.user.username + " Like" if self.like_dislike else " Dislike")

class Comment(models.Model):
    text = models.TextField( verbose_name=_("კომენტარი"))
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_("მომხმარებელი"))
    question = models.ForeignKey(Question,on_delete=models.CASCADE, verbose_name=_("კითხვა"), related_name="question")
    time = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return str(self.question.id) + " --> " + self.text


class FavoriteQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("მომხმარებელი"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("კითხვა"), related_name="favorite_question")

    def __str__(self):
        return self.user.username + " --> " + self.question.title