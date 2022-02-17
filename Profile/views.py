from django.views.generic import TemplateView,FormView,ListView,DetailView
from .models import Question,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.views.generic.edit import FormMixin


class ProfileHome(ListView):
    template_name = "profile/home.html"
    model = Question
    context_object_name = "question"


class QuestionDetail(FormView, DetailView):
    model = Question
    form_class = CommentForm
    context_object_name = "detail"
    queryset = Question.objects.all()
    success_url = "/"

    def get(self, request, *args, **kwargs):
        try:
            question = Question.objects.get(id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return redirect("Profile:home")
        return super(QuestionDetail, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object=self.get_form()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return super(QuestionDetail, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print("validuria")
        form.instance.user = self.request.user
        form.instance.question = self.get_object()
        form.save()
        return super(QuestionDetail, self).form_valid(form)

    def form_invalid(self, form):
        print("ara")
        return super(QuestionDetail, self).form_invalid(form)

class ERROR_404_VIEW(TemplateView):
    template_name = "profile/404error.html"
