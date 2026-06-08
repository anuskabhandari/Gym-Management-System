from django.urls import path
from subscription.api.views import (
    GymMemeberView,
    MembershipPayment,
    SubscriptionView,
    SubscriptionUpdateAndDelete
)


urlpatterns = [
     path('', SubscriptionView.as_view(), name='subscription'),
    path('<int:pk>/', SubscriptionUpdateAndDelete.as_view(), name='subscription-update-delete'),
    path('member',GymMemeberView.as_view()),
    path('payment/<int:id>',MembershipPayment.as_view())
]
