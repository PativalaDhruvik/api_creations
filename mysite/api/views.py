from django.shortcuts import render
from rest_framework import generics, status
from .models import Blogpost
from rest_framework.response import Response
from .serializers import Blogpostserializer
# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = Blogpostserializer

    def delete(self,request,*args,**kwargs):
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class updateDestroyView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Blogpost.objects.all()
     serializer_class = Blogpostserializer
     lookup_field = 'pk'


