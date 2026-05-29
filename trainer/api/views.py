from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from trainer.api.serializer import TrainerSerializer
from trainer.models import Trainer


class TrainerView(GenericAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    @extend_schema(
        responses=TrainerSerializer
    )
    def get(self, request):
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = TrainerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Member Successfully created"}, 201)
        else:
            return Response(serializer.errors, 422)
        
class TrainerUpdateAndDelete(GenericAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


    def put(self,request,pk):
        trainer= Trainer.objects.get(id=pk)
        data = request.data
        serializer = TrainerSerializer(trainer, data= data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                 "message":"Trainer Updated successfully"
                 })
        else:
            return Response(serializer.errors,422)
        
    def delete(self, request,pk):
        trainer = Trainer.objects.filter(id=pk)
        trainer.delete()
        return Response({
            "message":"Trainer deleted successfully"
        },204)    


        

