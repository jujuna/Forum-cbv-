from django.views.generic import TemplateView,FormView,ListView,DetailView
from .models import Question,Comment,Like,DisLike
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect,reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.views.generic.edit import FormMixin
from User.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import Http404



class ProfileHome(ListView):
    template_name = "profile/home.html"
    model = Question
    context_object_name = "question"


class QuestionDetail(FormView, DetailView):
    model = Question
    form_class = CommentForm
    context_object_name = "detail"

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except:
            return redirect('Profile:error')

        self.get_object()
        return super(QuestionDetail, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, *args, **kwargs):
        like_exist=bool(Like.objects.filter(user=self.request.user, question=self.get_object()))
        dislike_exist=bool(DisLike.objects.filter(user=self.request.user, question=self.get_object()))
        self.object=self.get_object()
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        try:
            question = Question.objects.get(id=self.kwargs["pk"])
            context['detail'] = question
            context['like_ex']=like_exist
            context['dislike_ex']=dislike_exist
        except Http404:
            return reverse("Profile:error")

        if "like" or "dislike" in self.request.GET:

            if "like" in self.request.GET:

                    if Like.objects.filter(user=self.request.user, question=self.get_object()):
                        Like.objects.filter(user=self.request.user, question=self.get_object()).delete()
                    else:
                        Like.objects.create(user=self.request.user, question=self.get_object())
                        if DisLike.objects.filter(user=self.request.user, question=self.get_object()):
                            DisLike.objects.filter(user=self.request.user, question=self.get_object()).delete()

            if "dislike" in self.request.GET:

                    if DisLike.objects.filter(user=self.request.user, question=self.get_object()).exists():
                        DisLike.objects.filter(user=self.request.user, question=self.get_object()).delete()
                    else:
                        DisLike.objects.create(user=self.request.user, question=self.get_object())
                        if Like.objects.filter(user=self.request.user, question=self.get_object()).exists():
                            Like.objects.filter(user=self.request.user, question=self.get_object()).delete()
            return redirect(reverse("Profile:home"))

        return context



    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = self.get_object()
        form.save()
        return super(QuestionDetail, self).form_valid(form)




class ERROR_404_VIEW(TemplateView):
    template_name = "profile/404error.html"