from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from attendance.models import Attendance
from attendance.api.serializer import AttendanceSerializer
class AttendanceView(GenericAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def patch(self,request,*args, **kwargs):
        print(kwargs)
        return Response({
            "message":"Patch request"
        })