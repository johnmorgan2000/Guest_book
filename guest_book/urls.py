from django.urls import path
from app import views

urlpatterns = [
    path('home/', views.GetHome.as_view(), name='home'),
    path('create/', views.Create.as_view(), name='create'),
]
