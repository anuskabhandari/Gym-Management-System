from member.models import Member
from member.api.serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def memberlist(request):
    data= Member.objects.all()
    serializer = MemberSerializer(data , many = True)
    return Response(serializer.data)

@api_view(['POST'])
def membercreate(request):
    post_data = request.data
    serializer = MemberSerializer(data=post_data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member Successfully created"
        },201)
    else:
        return Response(serializer.errors,422)
    

@api_view(['PUT'])
def memberupdate(request,id):
    member = Member.objects.get(id=id)
    serializer = MemberSerializer(member, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Member Successfully updated"
        }, status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['DELETE'])
def memberdelete(request,id):
    member = Member.objects.filter(id=id)
    member.delete()
    return Response({
        "message":"Member successfully deleted"
    }, 204)    