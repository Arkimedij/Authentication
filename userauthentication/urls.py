from django.contrib import admin
from django.urls import path
from userauthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('login/',views.cust_login, name = 'cust_login'),
    path('logout/',views.cust_login, name = 'cust_logout'),
    path('register/',views.register,name = 'register'),
    path('home/',views.dashboard, name = 'dashboard'),
]
