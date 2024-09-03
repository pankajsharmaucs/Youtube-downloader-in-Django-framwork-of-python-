from django.urls import include,path
from rest_framework import routers
from api.views import PostsViewSet
routers=routers.DefaultRouter()
routers.register(r'posts',PostsViewSet)

urlpatterns = [
    #api url
    path("",include(routers.urls)),
   
]