from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name="Profile"

urlpatterns = [
    path('', login_required(views.ProfileHome.as_view()), name='home'),
]
