from django.urls import path
from . import views

urlpatterns = [
    path('BlogPostList/',views.BlogPostListCreate.as_view(),name='BlogpostList')
]