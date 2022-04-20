from django.views.generic import TemplateView,FormView,ListView,DetailView,UpdateView
from .models import Question,Comment,Like,DisLike
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect,reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import CommentForm, QuestionForm
from django.views.generic.edit import FormMixin
from User.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Count, F


class ProfileHome(ListView):
    template_name = "Profile/home.html"
    model = Question
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.exclude(user=self.request.user)


class MyQuestions(ListView):
    template_name = "Profile/my_questions.html"
    model = Question
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

class TopQuestion(ListView):
    template_name = "Profile/top_question.html"
    model = Question
    context_object_name = "question"

    def get_queryset(self):
        return Question.objects.all().annotate(top_q=F('point')).order_by('-top_q')


class QuestionDetail(FormView, DetailView):
    model = Question
    form_class = CommentForm
    template_name = "Profile/question_detail.html"
    context_object_name = "detail"

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('Profile:error')

        self.get_object()
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, *args, **kwargs):
        like_exist=Like.objects.filter(user=self.request.user, question=self.get_object())
        dislike_exist=DisLike.objects.filter(user=self.request.user, question=self.get_object())

        self.object=self.get_object()
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        try:
            question = Question.objects.get(id=self.kwargs["pk"])
            context['owner'] = True if question.user == self.request.user else False
            context['detail'] = question
            context['like_ex'] = like_exist
            context['dislike_ex'] = dislike_exist
        except Http404:
            return reverse("Profile:error")

        if "like" or "dislike" in self.request.GET:

            like = Like.objects.filter(user=self.request.user, question=self.get_object())
            dislike = DisLike.objects.filter(user=self.request.user, question=self.get_object())

            if "like" in self.request.GET:

                    if like:
                        like.delete()
                    elif dislike:
                        Like.objects.create(user=self.request.user, question=self.get_object(), decrease=True)
                        DisLike.objects.filter(user=self.request.user, question=self.get_object()).delete()
                    else:
                        Like.objects.create(user=self.request.user, question=self.get_object(),decrease=False)

            if "dislike" in self.request.GET:

                    if dislike:
                        dislike.delete()
                    elif like:
                        DisLike.objects.create(user=self.request.user, question=self.get_object(), decrease=True)
                        Like.objects.filter(user=self.request.user, question=self.get_object()).delete()
                    else:
                        DisLike.objects.create(user=self.request.user, question=self.get_object(),decrease=False)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = self.get_object()
        form.save()
        return super(QuestionDetail, self).form_valid(form)


class AskQuestion(FormView):
    model = Question
    form_class = QuestionForm
    template_name = "Profile/question.html"
    context_object_name = "form"


    def get_success_url(self,):
        return reverse("Profile:question-detail", kwargs={"pk": self.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        self.pk = form.instance.id
        return super(AskQuestion, self).form_valid(form)

class UpdateQuestion(UpdateView):
    model = Question
    form_class = QuestionForm
    context_object_name = "form"
    template_name = "Profile/edit_question.html"
    success_url = "/"

class ERROR_404_VIEW(TemplateView):
    template_name = "Profile/404error.html"