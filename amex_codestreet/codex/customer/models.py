from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import User


# Create your models here.

class Customer_details(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    U_Bank_Id=models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    c_name= models.CharField(max_length=30)
    #p_date=models.DateTimeField(auto_now=True)
    c_number= models.CharField(max_length=30)
    
    c_address=models.CharField(max_length=30)
    c_age=models.CharField(max_length=30)
    c_income=models.CharField(max_length=30)

    def __str__(self):
         return f"{self.id} {self.U_Bank_Id} {self.c_name} {self.c_number} {self.c_address} {self.c_age} {self.c_income}"


class present_banking(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    b_due_amt_curr= models.BigIntegerField()
    
    b_balance=models.BigIntegerField() #done

    b_saving_monthly=models.BigIntegerField()

    b_total_savings=models.BigIntegerField()
    

    b_spend_mon1=models.BigIntegerField()
    b_spend_mon2=models.BigIntegerField()
    b_spend_mon3=models.BigIntegerField()
    b_spend_mon4=models.BigIntegerField()
    
    
    #amount calculated from the credit cards and loans
    b_due_amt_fut=models.BigIntegerField()

    #future income=present_income*6
    b_income_fut=models.BigIntegerField()

    b_debt_to_inc=models.FloatField()
    b_spend_to_save=models.FloatField()
    
    b_income=models.BigIntegerField()
    #from regression model
    b_spendings_fut=models.BigIntegerField()

    b_minimum=models.BigIntegerField()


    def __str__(self):
         return f"{self.id} {self.b_due_amt_curr} {self.b_balance} {self.b_saving_monthly} {self.b_total_savings} {self.b_spend_mon1} {self.b_spend_mon2} {self.b_spend_mon3} {self.b_spend_mon4} {self.b_due_amt_fut} {self.b_income_fut} {self.b_debt_to_inc}  {self.b_spend_to_save} {self.b_income} {self.b_spendings_fut} "


class future_banking(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    b_savings_opt=models.BigIntegerField()
    b_spend_opt=models.BigIntegerField()
    b_risk_score=models.FloatField()

    def __str__(self):
         return f"{self.id} {self.b_savings_opt} {self.b_spend_opt} {self.b_risk_score}"
    






