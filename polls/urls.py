from django.urls import path
from . import views

app_name = "polls" # this will namespace the URL to the polls app
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    path("<int:question_id>", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # Use the generic Class-based IndexView instead of the index view function
    # path("", views.IndexView.as_view(), name="index"),
    # Use the generic Class-based DetailView instead of the detail view function
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Use the generic Class-based ResultsView instead of the results view function
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]