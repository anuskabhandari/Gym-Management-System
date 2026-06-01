from django.urls import path
from attendance.api.views import AttendanceView
urlpatterns = [
    path('update/<int:id>', AttendanceView.as_view(), name="attendance-update"),
]