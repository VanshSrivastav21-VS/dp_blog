from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.login_view, name='register'),
    path('logout/', views.login_view, name='logout'),
    path('profile/', views.login_view, name='profile'),
]
