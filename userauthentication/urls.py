from django.contrib import admin
from django.urls import path
from userauthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register,name = 'register'),
    path('home/',views.dashboard, name = 'dashboard'),
]
