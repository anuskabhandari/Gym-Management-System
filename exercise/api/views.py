from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from exercise.models import (
    ExerciseCategory,
    Exercise,
    ExercisePlan,
    ExercisePlanDetail
)

from exercise.api.serializer import (
    ExerciseCategorySerializer,
    ExerciseSerializer,
    ExercisePlanSerializer,
    ExercisePlanDetailSerializer
)

@extend_schema(
    request=ExerciseCategorySerializer,
    responses=ExerciseCategorySerializer,
    tags=["ExerciseCategory"]
)
class ExerciseCategoryView(GenericAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

    def get(self, request):
        exercise_categories = ExerciseCategory.objects.all()
        serializer = ExerciseCategorySerializer(exercise_categories, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = ExerciseCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Exercise Category created successfully"}, 201)
        else:
         return Response(serializer.errors, 422)

@extend_schema(
    request=ExerciseCategorySerializer,
    responses=ExerciseCategorySerializer,
    tags=["ExerciseCategory"]
)

class ExerciseCategoryUpdateAndDelete(GenericAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

    def put(self,request,pk):
        exercise_categories = ExerciseCategory.objects.get(id=pk)
        data = request.data
        serializer = ExerciseCategorySerializer(exercise_categories, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"ExerciseCategory Updated successfully"
            })
        else:
            return Response(serializer.errors,422)

    def delete(self, request, pk):
        exercise_categories = ExerciseCategory.objects.filter(id=pk)
        if not exercise_categories.exists():
            return Response({
                "message": "ExerciseCategory not found"
            }, 404)
        exercise_categories.delete()
        return Response({
            "message": "ExerciseCategory deleted successfully"
        }, 204)

@extend_schema(
    request=ExerciseSerializer,
    responses=ExerciseSerializer,
    tags=["Exercise"]
)
class ExerciseView(GenericAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Exercise created successfully"}, status=status.HTTP_201_CREATED)
        else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=ExerciseSerializer,
    responses=ExerciseSerializer,
    tags=["Exercise"]
)      
class ExerciseUpdateAndDelete(GenericAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def put(self,request,pk):
        exercise = Exercise.objects.get(id=pk)
        data = request.data
        serializer = ExerciseSerializer(exercise, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Exercise Updated successfully"
            })
        else:
            return Response(serializer.errors,422)

    def delete(self, request, pk):
        exercise = Exercise.objects.filter(id=pk)
        if not exercise.exists():
            return Response({
                "message": "Exercise not found"
            }, 404)
        exercise.delete()
        return Response({
            "message": "Exercise deleted successfully"
        }, 204)

@extend_schema(
    request=ExercisePlanSerializer,
    responses=ExercisePlanSerializer,
    tags=["ExercisePlan"]
)
class ExercisePlanView(GenericAPIView):
    queryset = ExercisePlan.objects.all()
    serializer_class = ExercisePlanSerializer

    def get(self, request):
        plans = ExercisePlan.objects.all()
        serializer = ExercisePlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ExercisePlanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exercise Plan created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=ExercisePlanSerializer,
    responses=ExercisePlanSerializer,
    tags=["ExercisePlan"]
)       
class ExercisePlanUpdateAndDelete(GenericAPIView):
    queryset = ExercisePlan.objects.all()
    serializer_class = ExercisePlanSerializer

    def put(self,request,pk):
        plans = ExercisePlan.objects.get(id=pk)
        data = request.data
        serializer = ExercisePlanSerializer(plans, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"ExercisePlan Updated successfully"
            })
        else:
            return Response(serializer.errors,422)

    def delete(self, request, pk):
        plans = ExercisePlan.objects.filter(id=pk)
        if not plans.exists():
            return Response({
                "message": "ExercisePlan not found"
            }, 404)
        plans.delete()
        return Response({
            "message": "ExercisePlan deleted successfully"
        }, 204)

@extend_schema(
    request=ExercisePlanDetailSerializer,
    responses=ExercisePlanDetailSerializer,
    tags=["ExercisePlanDetail"]
)
class ExercisePlanDetailView(GenericAPIView):
    queryset = ExercisePlanDetail.objects.all()
    serializer_class = ExercisePlanDetailSerializer

    def get(self, request):
        details = ExercisePlanDetail.objects.all()
        serializer = ExercisePlanDetailSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data= request.data
        serializer = ExercisePlanDetailSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exercise Plan Detail created successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=ExercisePlanDetailSerializer,
    responses=ExercisePlanDetailSerializer,
    tags=["ExercisePlanDetail"]
)   
class ExercisePlanDetailUpdateAndDelete(GenericAPIView):
    queryset = ExercisePlanDetail.objects.all()
    serializer_class = ExercisePlanDetailSerializer

    def put(self,request,pk):
        details = ExercisePlanDetail.objects.get(id=pk)
        data = request.data
        serializer = ExercisePlanDetailSerializer(details, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"ExercisePlanDetail Updated successfully"
            })
        else:
            return Response(serializer.errors,422)

    def delete(self, request, pk):
        details = ExercisePlanDetail.objects.filter(id=pk)
        if not details.exists():
            return Response({
                "message": "ExercisePlanDetail not found"
            }, 404)
        details.delete()
        return Response({
            "message": "ExercisePlanDetail deleted successfully"
        }, 204)