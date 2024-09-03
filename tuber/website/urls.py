from django.urls import include,path
from . import views


urlpatterns = [
    #Wesite url
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('product/', views.product),
   
]