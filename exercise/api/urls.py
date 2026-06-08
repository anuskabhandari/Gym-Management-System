from django.urls import path

from exercise.api.views import ExerciseCategoryUpdateAndDelete, ExerciseCategoryView, ExercisePlanDetailUpdateAndDelete, ExercisePlanDetailView, ExercisePlanUpdateAndDelete, ExercisePlanView, ExerciseUpdateAndDelete, ExerciseView

urlpatterns = [
    # Exercise Category
    path('exercise-category/', ExerciseCategoryView.as_view(), name='exercise-category'),
    path('exercise-category/<int:pk>/', ExerciseCategoryUpdateAndDelete.as_view(), name='exercise-category-detail'),

    # Exercise
    path('exercise/', ExerciseView.as_view(), name='exercise'),
    path('exercise/<int:pk>/', ExerciseUpdateAndDelete.as_view(), name='exercise-detail'),

    # Exercise Plan
    path('exercise-plan/', ExercisePlanView.as_view(), name='exercise-plan'),
    path('exercise-plan/<int:pk>/', ExercisePlanUpdateAndDelete.as_view(), name='exercise-plan-detail'),

    # Exercise Plan Detail
    path('exercise-plan-detail/', ExercisePlanDetailView.as_view(), name='exercise-plan-detail'),
    path('exercise-plan-detail/<int:pk>/', ExercisePlanDetailUpdateAndDelete.as_view(), name='exercise-plan-detail-update'),
]