from django.contrib import admin
from django.urls import path, include

handler404 = 'website.views.custom_404'

urlpatterns = [
   #API 
   path('api/', include('api.urls')),
   
   #WEBSITE
   path('', include('website.urls')),
   path('home/', include('website.urls')),
   path('about/', include('website.urls')),
   path('product/', include('website.urls')),

    #Admin url
    path('admin/', admin.site.urls),
]