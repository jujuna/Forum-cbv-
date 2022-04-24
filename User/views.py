from django.views.generic import TemplateView, FormView
from .forms import UserForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.utils.decorators import method_decorator


class HomePage(TemplateView):
    template_name = "User/home.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Profile:home')
        return super(HomePage, self).get(request, *args, **kwargs)


class Registration(FormView):
    form_class = UserForm
    template_name = "User/registration.html"
    success_url = reverse_lazy("User:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Profile:home')
        return super(Registration, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(commit=True)
        return super(Registration, self).form_valid(form)


class Login(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("User:home")
    template_name = "User/login.html"
    success_url = reverse_lazy("Profile:home")

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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Profile:home')
        return super(Login, self).dispatch(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)