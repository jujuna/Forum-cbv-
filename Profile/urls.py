from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name="Profile"

urlpatterns = [
    path('', login_required(views.ProfileHome.as_view()), name='home'),
    path('404/', login_required(views.ERROR_404_VIEW.as_view()), name='error'),
    path('question/<int:pk>/', login_required(views.QuestionDetail.as_view()), name='question-detail'),
    path('ask/', login_required(views.AskQuestion.as_view()), name='question-form'),

]
