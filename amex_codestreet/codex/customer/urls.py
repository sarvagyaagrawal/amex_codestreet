from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_func, name='login_details'),
    path("logout", views.logout_view, name="logout"),
    path('register', views.register, name='register'),
    path('customer_dashboard', views.login_dashboard, name="dashboard"),
    path(r'^get_personal_info',views.get_personal_info, name="personal_details")

]