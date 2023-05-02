
from django.urls import path, include

from CoreApp import views
app_name = "CoreApp"
urlpatterns = [
    path('', views.home, name="core"),
    path('service/', views.service, name="service")
]
