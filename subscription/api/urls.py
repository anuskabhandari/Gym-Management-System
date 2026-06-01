from django.urls import path
from subscription.api.views import (
    GymMemeberView,
    SubscriptionView,
    SubscriptionUpdateAndDelete
)


urlpatterns = [
     path('', SubscriptionView.as_view(), name='subscription'),
    path('<int:pk>/', SubscriptionUpdateAndDelete.as_view(), name='subscription-update-delete'),
    path('member',GymMemeberView.as_view())
]
