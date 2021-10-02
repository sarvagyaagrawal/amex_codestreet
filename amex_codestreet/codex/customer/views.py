from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.contrib.auth.models import User
from .models import Customer_details
from django.template import Context, Engine, TemplateDoesNotExist, loader
from urllib.parse import quote

######################################################################

#function for logout
def index(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return HttpResponseRedirect(reverse("login_details"))

#######################################################################


def fetchdata(request):
    customer_det=Customer_details.objects.filter(user=request.user)
    return customer_det
####################################################################
#This function is used when user logs in!  
def login_dashboard(request):
    if request.user.is_authenticated:
        try:
            cust=Customer_details.objects.get(user=request.user)
            cust1=fetchdata(request)

            return render(request, 'customer/dashboard.html',{
                "message": "Welcome to CODEX! ",
                "cust":cust1
            })
        except Customer_details.DoesNotExist:
            return render(request, 'customer/dashboard.html',{
                "message": "Welcome to CODEX! ",
                "message1":"Please fill out your Personal Information to view your Unique Bank ID"
            })
    else:
        return HttpResponseRedirect(reverse("login_details"))

#Function for logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def login_func(request):

    if request.method=="POST":
        
        username=request.POST.get('username')
        password=request.POST.get('password')   

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'customer/login.html', {
                "message": "Invalid username and/or password."
            })
    
    else:
        return render(request, 'customer/login.html')

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        confirm=request.POST["c_password"]
        email=request.POST["email"]
        
        if username is None or username=='':
            return render(request,"customer/register.html", {
                    "message": "Username not entered."
                })
        elif password is None or password=='':
            return render(request,"customer/register.html", {
                    "message": "Password not entered"
                })
        elif confirm is None or confirm=='':
            return render(request,"customer/register.html", {
                    "message": "Confirm Password not entered"
                })
        elif email is None or email=='':
            return render(request,"customer/register.html", {
                    "message": "Email not entered"
                })
        if username is not None:
            if password!=confirm:
                return render(request,"customer/register.html", {
                    "message": "Passwords must match."
                })
        
        
        try:
            user=User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            return render(request, "customer/register.html", {
                "message": "Username/Email address already exists."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "customer/register.html")
####################################################################



####################################################################

''' Function to get values for Personal data from customer'''

@csrf_exempt
@login_required
def get_personal_info(request):

    if request.method=="POST":
        cust_name=request.POST.get('your_name')
        cust_number=request.POST.get('your_contact')
        cust_address=request.POST.get('your_address')
        cust_age=request.POST.get('your_age')
        cust_income=request.POST.get('your_income')


        if cust_name is None or cust_name=='':
            return render(request, 'customer/dashboard.html', {
            "message": "Please enter Name"
        })
        elif cust_number is None or cust_number=='':
            return render(request, 'customer/dashboard.html', {
            "message": "Please enter Contact Number"
        })
        elif cust_address is None or cust_address=='':
            return render(request, 'customer/dashboard.html', {
            "message": "Please enter Address"
        })
        elif cust_age is None or cust_age=='':
            return render(request, 'customer/dashboard.html', {
            "message": "Please enter Address"
        })
        elif cust_income is None or cust_income=='':
            return render(request, 'customer/dashboard.html', {
            "message": "Please enter Address"
        })
        else:
            try:
                cust=Customer_details.objects.get(user=request.user)
                cust.c_name=cust_name
                cust.c_age=cust_age
                cust.c_address=cust_address
                cust.c_number=cust_number
                cust.c_income=cust_income
                cust.save()
                customer_det=fetchdata(request)
                return render(request, 'customer/dashboard.html', {
                     "message": "Your Personal Information has been updated successfully!",
                     "cust":customer_det
                })

            except Customer_details.DoesNotExist:
                c_details=Customer_details(user=request.user,c_name=cust_name,c_age=cust_age,c_address=cust_address, c_number=cust_number, c_income=cust_income)
                c_details.save()
                customer_det=fetchdata(request)
                return render(request, 'customer/dashboard.html', {
                     "message": "Your Personal Information has been submitted successfully!",
                     "cust":customer_det
                })
    else:
        return render(request, 'pcustomer/dashboard.html',{
            "message":"Some error occurred. Please try again!"
        })





       

        


        
        
