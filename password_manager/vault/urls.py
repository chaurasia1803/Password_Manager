from django.urls import path
from .views import password_list, add_password, reveal_password
from . import views


app_name = "vault"

urlpatterns = [
    path('passwords/', views.password_list, name='password_list'),
    path('add/', views.add_password, name='add_password'),
    path("reveal/<int:pk>/", views.reveal_password, name='reveal_password'),
]