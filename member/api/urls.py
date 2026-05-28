from django.urls import path
from member.api.views import memberlist

urlpatterns = [
    path('', memberlist,name = "member-list")
]
