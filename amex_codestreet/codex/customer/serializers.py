from rest_framework import serializers 
from .models import Customer_details, present_banking, future_banking 

class CustomerSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Customer_details 
        fields='__all__'

class present_bankingSerializers(serializers.ModelSerializer): 
    class meta: 
        model=present_banking 
        fields='__all__'

class future_bankingSerializers(serializers.ModelSerializer): 
    class meta: 
        model=future_banking 
        fields='__all__'