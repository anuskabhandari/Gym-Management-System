from django.urls import path

from trainer.api.views import TrainerView ,TrainerUpdateAndDelete


urlpatterns = [
    path('', TrainerView.as_view(), name="trainer"),
     path('<int:pk>', TrainerUpdateAndDelete.as_view(),name="Trainer-update")
]
