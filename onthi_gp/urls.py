from django.urls import path
from . import views

app_name = "onthi_gp"
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:chu_de>/', views.onthi, name='index'),
]