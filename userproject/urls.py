
from django.contrib import admin
from django.urls import path
from home.views import index,loginuser,logoutuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="home"),
    path('login', loginuser, name='login'),
    path('logout', logoutuser, name='logout'),
]
