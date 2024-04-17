from rest_framework import generics, status
from rest_framework.response import Response
from .models import blogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = blogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        blogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostUpdateDestroyRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
