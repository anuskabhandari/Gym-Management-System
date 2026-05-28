from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from trainer.api.serializer import TrainerSerializer
from trainer.models import Trainer


class TrainerView(GenericAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

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