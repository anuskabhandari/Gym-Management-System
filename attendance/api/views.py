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
    
    def patch(self, request, *args, **kwargs):
        data = request.data
        attendance_data = Attendance.objects.get(id=kwargs["id"])
        serializer = AttendanceSerializer(
            attendance_data, data=data, context={"attendance_data": attendance_data, 'sunway':True}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"})
        else:
            return Response(serializer.errors)