from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('adminuser/',views.adminuser,name="adminuser"),
    path('customer/',views.customer,name="customer"),
    path('employee/',views.employee,name="employee"),
    path('student/',views.student,name="student"),
    
]