from django.db import models

# Create your models here.
import uuid
# Create your models here.
from django.contrib.auth.models import User


class Credit_Card(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    due_amt=models.IntegerField()
    int_rate=models.IntegerField()
    mini_amt=models.IntegerField()

    def __str__(self):
         return f"{self.id} {self.due_amt} {self.int_rate} {self.mini_amt}"


class loan_details(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    due_amt=models.IntegerField()
    int_rate=models.IntegerField()
    mini_amt=models.IntegerField()
    loan_amt=models.IntegerField()

    def __str__(self):
         return f"{self.id} {self.due_amt} {self.int_rate} {self.mini_amt} {self.loan_amt}"

class withdrawl(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    amt1=models.IntegerField()
    amt2=models.IntegerField()
    amt3=models.IntegerField()
    amt4=models.IntegerField()

    def __str__(self):
         return f"{self.id} {self.amt1} {self.amt2} {self.amt3} {self.amt4}"
class Bank_customer(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    UBI=models.UUIDField(null=True,max_length=100,blank=True)
    permission=models.BooleanField(null=True, max_length=30)
    cust_ID=models.CharField(max_length=30)
    credit=models.ForeignKey(Credit_Card,null=True, on_delete=models.CASCADE)
    loan=models.ForeignKey(loan_details,null=True, on_delete=models.CASCADE)
    balance=models.IntegerField(null=True)
    amt_withdraw=models.ForeignKey(withdrawl,null=True, on_delete=models.CASCADE)

    def __str__(self):
         return f"{self.id} {self.UBI} {self.permission} {self.cust_ID} {self.credit} {self.loan}"



