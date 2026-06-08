from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import (
    ExerciseCategory,
    Exercise,
    ExercisePlan,
    ExercisePlanDetail
)


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "muscle_group",
        "difficulty"
    )
    search_fields = ("name", "muscle_group")


@admin.register(ExercisePlan)
class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "plan_name",
        "member",
        "trainer",
        "goal"
    )


@admin.register(ExercisePlanDetail)
class ExercisePlanDetailAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "plan",
        "exercise",
        "day_of_week",
        "sets",
        "reps"
    )