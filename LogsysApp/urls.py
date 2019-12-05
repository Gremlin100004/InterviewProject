from django.urls import path
from LogsysApp import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.registration),
]
