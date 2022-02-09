from django.urls import path

from . import views

app_name="User"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('reg/', views.Registration.as_view(), name='registration'),
    path('log/', views.Login.as_view(), name='login'),
    path("logout/",views.Logout.as_view(),name="logout")
]