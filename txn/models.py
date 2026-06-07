from django.db import models
class Status(models.TextChoices):
    INITIAL ="Initial"
    COMPLETED ="Completed"
    PENDING = "Pendindg"
    USER_CANCELLED = "User canceled"
# Create your models here.
class TXN(models.Model):
    member = models.ForeignKey('member.Member',on_delete= models.RESTRICT)
    name = models.CharField(max_length=100, blank= True)
    amount= models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20, choices= Status.choices, default = Status.INITIAL)
    txn_id = models.CharField(max_length=50, blank= True, null = True)
    pidx = models.CharField(max_length=30, blank= True, null = True)
    location = models.TextField(null = True,blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

