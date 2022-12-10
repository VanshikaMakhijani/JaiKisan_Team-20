from django.urls import path
from . import views

urlpatterns = [
     path('home/',views.homePage,name='homePage'),
     path('farmerRegister/',views.registerFarmer, name='registerFrame'),
     path('farmerDetails/',views.farmerDetails,name='farmerDetails'),
     path('executiveRegister/',views.executiveRegister,name='executiveRegister'),
     path('executiveDetails/',views.executiveDetails,name='executiveDetails'),


     

]
