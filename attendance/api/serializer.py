from rest_framework import serializers

from attendance.models import Attendance

from datetime import datetime
from rest_framework.validators import ValidationError
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['member', 'check_in', 'check_out']

    def validate_member(self, member):
        attendance_data = self.context["attendance_data"]
        if attendance_data.member != member:
            raise ValidationError("Member doesnot match")
        return member

    def validate(self, attrs):
        attendance_data = self.context["attendance_data"]
        today_date = datetime.now().date()

        if attendance_data.attendance_date != today_date:
            raise ValidationError("Date doesnot match")

        if "check_in" in attrs.keys() and "check_out" in attrs.keys():
            raise ValidationError("we can't send check in and checkout at same time")

        elif "check_in" in attrs.keys():
            if attendance_data.check_in:
                raise ValidationError("Already check in")

        elif "check_out" in attrs.keys():
            if attendance_data.check_in is None:
                raise ValidationError("Please check in first")

            elif attendance_data.check_out:
                raise ValidationError("Already checkout")

        return attrs