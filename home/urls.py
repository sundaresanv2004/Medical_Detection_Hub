from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/<str:pk>', views.upload, name='upload'),
    path('result/<str:pk1>', views.result, name='result'),
]