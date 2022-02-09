from django.views.generic import TemplateView,FormView
from .forms import UserForm,AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect

class HomePage(TemplateView):
    template_name = "user/home.html"


class Registration(FormView):
    form_class = UserForm
    template_name = "user/registration.html"
    success_url = reverse_lazy("User:home")

    def form_valid(self, form):
        form.save(commit=True)
        return super(Registration, self).form_valid(form)


class Login(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("User:home")
    template_name = "user/login.html"

    def form_valid(self, form):
        email = self.request.POST.get("username","")
        password = self.request.POST.get("password","")
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(Login, self).form_invalid(form)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)