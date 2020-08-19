from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^demo1/', views.demo1),
]