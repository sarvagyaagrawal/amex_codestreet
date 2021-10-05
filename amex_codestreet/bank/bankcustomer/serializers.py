from rest_framework import serializers

from .models import Credit_Card,loan_details,Bank_customer,withdrawl

class Credit_CardSerializer(serializers.ModelSerializer):
    due_amt=serializers.IntegerField()
    int_rate=serializers.IntegerField()
    mini_amt=serializers.IntegerField()

    class Meta:
        model = Credit_Card
        fields = ('__all__')

class loan_detailsSerializer(serializers.ModelSerializer):
    due_amt=serializers.IntegerField()
    int_rate=serializers.IntegerField()
    mini_amt=serializers.IntegerField()

    class Meta:
        model = loan_details
        fields = ('__all__')

class withdrawlSerializer(serializers.ModelSerializer):
    amt1=serializers.IntegerField()
    amt2=serializers.IntegerField()
    amt3=serializers.IntegerField()
    amt4=serializers.IntegerField()

    class Meta:
        model = withdrawl
        fields = ('__all__')
class Bank_customerSerializer(serializers.ModelSerializer):
    UBI=serializers.UUIDField()
    permission=serializers.BooleanField()
    cust_ID=serializers.CharField()
    credit=Credit_CardSerializer()
    loan=loan_detailsSerializer()
    balance=serializers.IntegerField()
    amt_withdraw=withdrawlSerializer()

    class Meta:
        model = Bank_customer
        fields = ('__all__')
        depth = 2