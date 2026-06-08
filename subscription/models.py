from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=30)
    days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscription"


class MembershipStatus(models.TextChoices):
     ACTIVE = "Active"
     INACTIVE = "Inactive"
class GymMembership(models.Model):

   

     trainer = models.ForeignKey("trainer.Trainer",on_delete=models.CASCADE, null = True , blank = True)
    
     member = models.ForeignKey("member.Member",on_delete=models.CASCADE)
     subscription = models.ForeignKey("Subscription",on_delete=models.CASCADE)
     days = models.PositiveIntegerField()
     price =  models.DecimalField(max_digits=10, decimal_places=2)
     status = models.CharField(max_length=20, choices=MembershipStatus.choices, default=MembershipStatus.INACTIVE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
      return f'{self.subscription}'

     class Meta:
        db_table = "gymmembership"




    

