from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',views.AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/comment',views.AddCommentView.as_view(), name='add_comment'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',views.DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>',views.LikeView, name='like_post'),
   
  
]