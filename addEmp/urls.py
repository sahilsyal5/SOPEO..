from django.urls import path 
from . import views 

urlpatterns = [  
    path('',views.addemp,name='addemp'),
]