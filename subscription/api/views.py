from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from subscription.api.serializer import GymMembershipSerializer, SubscriptionSerializer
from subscription.models import GymMembership, Subscription

class SubscriptionView(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    @extend_schema(
        responses= SubscriptionSerializer
    )
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many = True)
        return Response(serializer.data , 200)
    

    def post(self , request):
        data = request.data
        serializer = SubscriptionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Subscription created successfully"},
                201
            )
        else: 
            return Response(serializer.errors , 422)
        
class SubscriptionUpdateAndDelete(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def put(self, request, pk):
        subscription = Subscription.objects.get(id=pk)
        data = request.data

        serializer = SubscriptionSerializer(subscription , data = data)   

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message" : "Subscription updated Successfully"

            })  
        else:
            return Response(serializer.errors , 422)

    def delete(self , request,pk):
        subscription = Subscription.objects.fileter(id=pk)
        subscription.delete()

        return Response({
            "message":"Subscription deleted successfully"
        },204)
    


@extend_schema(
    request=GymMembershipSerializer,
    responses=GymMembershipSerializer,
    tags=["Gymmembership"]
)
class GymMemeberView(GenericAPIView):
    queryset = GymMembership.objects.all()
    serializer_class = GymMembershipSerializer


    def get(self, request):
        data = GymMembership.objects.all()
        serializer = GymMembershipSerializer(data, many=True)
        return Response(serializer.data, 200) 

    def post(self,request):
        data = request.data
        serializer = GymMembershipSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "GymMemebership  Successfully created"}, 201)
        else:
            return Response(serializer.errors, 422)    
    



