from django.contrib import admin
from .models import Customer_details,present_banking, future_banking
# Register your models here.

admin.site.register(Customer_details)
admin.site.register(present_banking)
admin.site.register(future_banking)
