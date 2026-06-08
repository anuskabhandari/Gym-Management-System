from rest_framework import serializers

from exercise.models import (
    ExerciseCategory,
    Exercise,
    ExercisePlan,
    ExercisePlanDetail
)


class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class ExercisePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlan
        fields = '__all__'


class ExercisePlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlanDetail
        fields = '__all__'