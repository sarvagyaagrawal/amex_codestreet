from django.contrib import admin
from .models import Credit_Card,loan_details,Bank_customer, withdrawl
# Register your models here.

admin.site.register(Credit_Card)
admin.site.register(loan_details)
admin.site.register(Bank_customer)
admin.site.register(withdrawl)