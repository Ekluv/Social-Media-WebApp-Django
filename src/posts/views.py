from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from .models import Post, Like
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_comments.models import Comment
from .forms import PostForm, LikeForm


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


class LikeFormView(FormView):
    form_class = LikeForm

    def form_valid(self,form):
        print form.data
        post = get_object_or_404(Post,pk=form.data["posts"])
        user= self.request.user
        prev_likes= Like.objects.filter(voter=user,post=post)
        has_voted = (prev_likes.count() >0)
        if not has_voted:
            Like.objects.create(voter=user,post=post)
        return redirect("post_list")

    def form_invalid(self,form):
        print form
        return redirect("home")


