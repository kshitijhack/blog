from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, CommentCreateView,trial, CategoryDetailView

app_name = 'posts'

urlpatterns = [
  
  path('posts/', PostListView.as_view(), name='post-list'),
  path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('posts/create/', PostCreateView.as_view(), name='post-create'),
  path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('posts/<int:pk>/comment/', CommentCreateView.as_view(), name='post-comment'),
  path('posts/category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
  path('index/', trial),

 
]