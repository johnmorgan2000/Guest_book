from django.urls import path
from app import views

urlpatterns = [
    path('/', views.Add.as_view(), name='home'),
]
