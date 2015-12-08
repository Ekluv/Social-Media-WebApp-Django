from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_comments.models import Comment

# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self,*args,**kwargs):
        qs=super(PostListView,self).get_queryset(*args,**kwargs)
        query=self.request.GET.get('q')
        print query
        if query:
            qs=self.model.objects.filter(submitted_by__username=query)
        else:
            qs=self.model.objects.filter(submitted_by=self.request.user)
        return qs

class PostDetailView(DetailView):
    model = Post
