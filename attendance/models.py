from django.db import models

# Create your models here.
class Attendance(models.Model):
    member = models.ForeignKey('Member', on_delete= models.CASCADE),
    check_in = models.TimeField(null = True , blank = True)
    check_out = models.DateTimeField(null=True, blank=True)

    attendance_date = models.DateField()

    is_present = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name}"
    
    class Meta:
        db_table = 'attendance'