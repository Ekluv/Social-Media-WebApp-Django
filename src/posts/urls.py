__author__ = 'Ekluv'
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import PostListView,PostDetailView,LikeFormView

urlpatterns = [
    # Examples:

    url(r'^$',PostListView.as_view() , name='post_list'),
     url(r'^comments/', include('django_comments.urls')),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view() ,name="post_detail"),
    url(r'^addpost$','posts.views.addpost' , name='add_post'),
    url(r'^like$',LikeFormView.as_view() , name='like'),


]
