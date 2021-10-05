from django.db.models.fields import UUIDField
from django.test import TestCase
import requests
import json
# Create your tests here.
response=requests.get("http://127.0.0.1:8000/bank/db400ec5-f390-4d2a-af90-fad095207402?format=json")
getdata=response.json()

print(type(int(getdata["data"]["credit"]["due_amt"])))