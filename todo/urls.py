from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home', views.index, name="index"),
    path('edit/<str:pk>/', views.edit, name="edit"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('reg', views.register, name="register"),
    path('', views.login, name="login"),
    # path('logout', views.logout, name="logout"),
]
