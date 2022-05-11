from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name="Profile"

urlpatterns = [
    path('', login_required(views.ProfileHome.as_view()), name='home'),
    path('404/', login_required(views.ERROR_404_VIEW.as_view()), name='error'),
    path('question/<int:pk>/', login_required(views.QuestionDetail.as_view()), name='question-detail'),
    path('ask/', login_required(views.AskQuestion.as_view()), name='question-form'),
    path('my-questions/', login_required(views.MyQuestions.as_view()), name='my-question'),
    path('top-questions/', login_required(views.TopQuestion.as_view()), name='top-question'),
    path('update/<int:pk>/', login_required(views.UpdateQuestion.as_view()), name='update-question'),
    path('update-profile/<int:pk>/', login_required(views.UpdateUserProfile.as_view()), name='update-profile'),
    path('favourite/', login_required(views.FavouriteQuestion.as_view()), name='fav'),
    path('searched/', login_required(views.SearchedResult.as_view()), name='search'),

]
