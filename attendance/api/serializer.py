from rest_framework import serializers

from attendance.models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
         model = Attendance
         fields = ['member','check_in','check_out']
