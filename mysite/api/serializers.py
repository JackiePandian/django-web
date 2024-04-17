from rest_framework import serializers
from .models import blogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogPost
        fields = ['id', 'title', 'content', 'published_date']