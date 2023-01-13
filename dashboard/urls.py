from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('display/', views.display, name='viewallcustomer'),    
    path('transfer/', views.transfer, name='transfer'),  
    path('transferDetails/', views.transferDetails, name='transferdetails'),     
       
     
        
]
