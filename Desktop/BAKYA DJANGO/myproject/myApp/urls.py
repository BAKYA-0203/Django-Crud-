from . import views
from django.urls import path
urlpatterns = [

    path('',views.home,name="home"),
    path('addemp/',views.addemp,name="addemp"),
    path('viewemp/',views.viewemp,name="viewemp"),
    path('update/<int:id>',views.update),
    path('upemp/<int:id>',views.upemp),
    path('delemp/<int:id>',views.delemp),
    path('profile1/<int:id>',views.profile1,name="profile1")
   
]