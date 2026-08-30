from django.shortcuts import render
from rest_framework import generics
from .models import Blogpost
from .serializers import Blogpostserializer
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = Blogpostserializer
