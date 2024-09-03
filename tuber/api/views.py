
from rest_framework import viewsets
from api.serializers import PostsSerializer
from api.models import Posts

class PostsViewSet(viewsets.ModelViewSet):
    queryset=Posts.objects.all()
    serializer_class=PostsSerializer



