from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_teacher, name='register_teacher'),
    path('login/', views.login_teacher, name='login_teacher'),
    path('logout/', views.logout_teacher, name='logout_teacher'),
]
