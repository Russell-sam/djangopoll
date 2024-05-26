from django.urls import path
from . import views

app_name= "mypoll"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail-page"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results-page"),
    path("<int:question_id>/vote/", views.vote, name="vote-page"),
]