from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('booking/<int:room_id>/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('rooms/', views.rooms, name='rooms'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('deluxe/', views.deluxe_rooms, name='deluxe'),
    path('luxury/', views.luxury_rooms, name='luxury'),
   


    







]
