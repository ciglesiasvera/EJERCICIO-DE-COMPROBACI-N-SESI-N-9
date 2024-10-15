from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from .views import input_book

def logout_then_login(request):
    auth_views.logout_then_login(request)
    return redirect('login')

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='book/login.html'), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('inputbook/', input_book, name='inputbook'),
]