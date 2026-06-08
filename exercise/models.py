
from django.db import models

# Create your models here.


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "exercisecategory"


class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    )

    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=150)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100, blank=True)
    calories_burned = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "exercise"


class ExercisePlan(models.Model):
    GOAL_CHOICES = (
        ("Weight Loss", "Weight Loss"),
        ("Muscle Gain", "Muscle Gain"),
        ("Fat Loss", "Fat Loss"),
        ("Strength", "Strength"),
    )

    member = models.ForeignKey("member.Member", on_delete=models.CASCADE)
    trainer = models.ForeignKey("trainer.Trainer", on_delete=models.SET_NULL, null=True)
    plan_name = models.CharField(max_length=200)
    goal = models.CharField(max_length=50, choices=GOAL_CHOICES)

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.plan_name
    
    class Meta:
        db_table = "exerciseplan"


class ExercisePlanDetail(models.Model):
    DAYS = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    )

    plan = models.ForeignKey(ExercisePlan, on_delete=models.CASCADE, related_name="plan_details")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAYS)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"{self.exercise.name}"
    
    class Meta:
        db_table = "exerciseplandetail"