
from django.urls import path
from graceapp import views


urlpatterns = [
        path('',views.base),
        path('home/',views.home),
        path('index/',views.index),
        
]


