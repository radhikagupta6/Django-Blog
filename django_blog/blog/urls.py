from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',views.AddPostView.as_view(), name='add_post'),
    path('add_category/',views.AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>',views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',views.DeletePostView.as_view(), name='delete_post'),
]