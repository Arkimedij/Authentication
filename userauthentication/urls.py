from django.contrib import admin
from django.urls import path
from userauthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name = 'login'),
    path('',views.register,name = 'register'),
    path('home/',views.home, name = 'home'),
]
