from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_comments.models import Comment
from .forms import PostForm


# Create your views here.

class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        qs = super(PostListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        print query
        if query:
            qs = self.model.objects.filter(submitted_by__username=query)
        else:
            qs = self.model.objects.filter(submitted_by=self.request.user)
        return qs


class PostDetailView(DetailView):
    model = Post


def addpost(request):
    msg = 'Add a Post'
    form = PostForm(request.POST or None)
    form.submitted_by = request.user
    print form.submitted_by
    context = {
        "msg": msg,
        "form": form,
        "button_value":"Submit post"
    }
    if form.is_valid():
        print form
        instance = form.save(commit=False)
        instance.submitted_by= request.user
        instance.save();
        context = {
        "msg": "Post submitted successfully",
        "button_value": "Add More"
        }

    return render(request, "posts/addpost.html", context)


