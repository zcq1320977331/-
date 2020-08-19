from django.urls import path
from . import views
urlpatterns = [
    path('homedb/', views.homedb),
]