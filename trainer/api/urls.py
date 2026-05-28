from django.urls import path

from trainer.api.views import TrainerView


urlpatterns = [
    path('', TrainerView.as_view(), name="trainer")
]
