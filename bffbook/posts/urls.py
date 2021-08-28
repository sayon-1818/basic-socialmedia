from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import PostDeleteView, PostUpdateView
app_name="posts"

urlpatterns =[
    path('', views.post_comment_create_and_list_view, name="main-post-view"),
    path('liked/', views.like_unlike_post, name="like-post-view"),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
]