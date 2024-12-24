from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'launches'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='launches/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.search_launches, name='search_launches'),
    path('about/', views.about, name='about'),
]
