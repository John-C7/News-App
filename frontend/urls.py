from django.urls import path
from frontend import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('next', views.loadcontent, name="Loadcontent"),
]