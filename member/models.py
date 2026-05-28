from django.db import models

# Create your models here.
class GenderChoice(models.TextChoices):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

class BloodGroup(models.TextChoices):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=5, choices=GenderChoice.choices)
    emergency_contact = models.PositiveBigIntegerField(default=0)
    address = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    joined_at = models.DateField()
    height_cm = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    weight_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    blood_group = models.CharField(max_length=5, choices=BloodGroup.choices, null=True, blank=True)
    medical_conditions = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'member'

    def _str_(self):
        return self.first_name