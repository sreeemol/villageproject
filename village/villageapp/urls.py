from . import views
from django.urls import path



app_name = 'villageapp'

urlpatterns = [
	 path('',views.index,name='index'),
	 path('register_panchayath/',views.register_panchayath,name='register_panchayath'),
	 path('register_employees/',views. register_employees,name='register_employees'),
     path('register_enduser/',views. register_enduser,name='register_enduser'),
	 path('register_Leaveapplication/',views. register_Leaveapplication,name='register_Leaveapplication'),
     path('register_Complaint/',views. register_Complaint,name='register_Complaint'),
	 path('register_News/',views. register_News,name='register_News'),
	 path('register_Salary/',views. register_Salary,name='register_Salary')

     
]