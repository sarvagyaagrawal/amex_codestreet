from django.urls import path

from . import views
from .views import DataView

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_func, name='login_details'),
    path("logout", views.logout_view, name="logout"),
    path('register', views.register, name='register'),
    path(r'customer_dashboard/', views.login_dashboard, name="dashboard"),
    path(r'customer_dashboard/enterUBI', views.enterUBI, name="enterUBI"),
    path('bank/<uuid:id>', DataView.as_view())
]