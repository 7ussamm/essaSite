from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logout, name='logout'),
    path('content/', views.content, name='content'),

]