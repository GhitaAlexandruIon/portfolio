from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<pk>/remove', views.post_remove, name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('email/', views.emailview, name='email'),
    path('success', views.successview, name='success'),
]
