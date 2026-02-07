from django.urls import path 
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('admin_login/',views.admin_login,name='authontication_admin'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    
]