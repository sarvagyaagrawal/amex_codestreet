from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.contrib.auth.models import User
from django.template import Context, Engine, TemplateDoesNotExist, loader
from urllib.parse import quote
from .models import Credit_Card,loan_details,Bank_customer,withdrawl
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Credit_CardSerializer,loan_detailsSerializer,withdrawlSerializer,Bank_customerSerializer
######################################################################

def index(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return HttpResponseRedirect(reverse("login_details"))

#######################################################################
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

#######################################################################
def login_func(request):

    if request.method=="POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')   

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'bankcustomer/login.html', {
                "message": "Invalid username and/or password."
            })
    
    else:
        return render(request, 'bankcustomer/login.html')

#######################################################################
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        confirm=request.POST["c_password"]
        email=request.POST["email"]
        
        if username is None or username=='':
            return render(request,"bankcustomer/register.html", {
                    "message": "Username not entered."
                })
        elif password is None or password=='':
            return render(request,"bankcustomer/register.html", {
                    "message": "Password not entered"
                })
        elif confirm is None or confirm=='':
            return render(request,"bankcustomer/register.html", {
                    "message": "Confirm Password not entered"
                })
        elif email is None or email=='':
            return render(request,"bankcustomer/register.html", {
                    "message": "Email not entered"
                })
        if username is not None:
            if password!=confirm:
                return render(request,"bankcustomer/register.html", {
                    "message": "Passwords must match."
                })
        
        
        try:
            user=User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            return render(request, "bankcustomer/register.html", {
                "message": "Username/Email address already exists."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "bankcustomer/register.html")

####################################################################

def login_dashboard(request):
    if request.user.is_authenticated:
        try:
            person=Bank_customer.objects.get(user=request.user)
            cust=Bank_customer.objects.filter(user=request.user)
            return render(request, 'bankcustomer/dashboard_login.html',{
                "message": "Welcome to Fin Bank! ",
                "cust":cust
            })
        except Bank_customer.DoesNotExist:
            return render(request, 'bankcustomer/dashboard_login.html',{
                "message": "Welcome to Fin Bank! ",
                "message1":"No information available in Database!"
                
            })
        
    else:
        return HttpResponseRedirect(reverse("login_details"))

#######################################################################
@csrf_exempt
@login_required
def enterUBI(request):
    if request.method=="POST":
        UBI=request.POST["fill_UBI"]

        if UBI is None or UBI=='' or len(UBI)!=36:
            return render(request, 'bankcustomer/dashboard_login.html', {
            "message": "Incorrect UBI entered! Please enter the correct value."
        })
        else:
            try:
                person=Bank_customer.objects.get(user=request.user)
                
                person.UBI=UBI
                person.permission=True
                person.save()
                cust=person=Bank_customer.objects.filter(user=request.user)
                return render(request, 'bankcustomer/dashboard_login.html', {
                    "message": "Successfully Submitted UBI!",
                    "cust":cust
                })
            except Bank_customer.DoesNotExist:
                return render(request, 'bankcustomer/dashboard_login.html', {
                    "message": "Uh! Your Information not found in Database!"
                })
    else:
        return render(request, 'bankcustomer/dashboard_login.html', {
                    "message": "Sorry! Some error occured!"
                })
########################################################################

class DataView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                person=Bank_customer.objects.get(UBI=id)
                
                if person.permission=='No':
                    return Response({"status": "access not provided"})
                else:
                    serializer = Bank_customerSerializer(person)
                    return Response({"status": "success", "data": serializer.data})

            except Bank_customer.DoesNotExist:
                return Response({"status": "failure"})
        else:
            return Response({"status": "failure"})