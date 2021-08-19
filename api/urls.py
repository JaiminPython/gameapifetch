from django.urls import path

from api.views import APIForGame

urlpatterns = [
    path('search_game/', APIForGame.as_view()),
]
