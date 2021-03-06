from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_func, name='login_details'),
    path("logout", views.logout_view, name="logout"),
    path('register', views.register, name='register'),
    path(r'customer_dashboard/', views.login_dashboard, name="dashboard"),
    path(r'customer_dashboard/personal/',views.get_personal_info, name="personal_details"),
    path(r'customer_dashboard/riskfactor/',views.riskfactor, name="riskfactor"),
    path(r'customer_dashboard/generate_data_from_bank/',views.generate_data_from_bank, name="generate_data_from_bank")

]