from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('<str:username>/posts/new', views.createPost, name='newPost'),
    path('<str:username>/posts/<int:id>/delete', views.deletePost, name='deletePost'),     
    path('<str:username>/posts/<int:id>/update', views.updatePost, name='updatePost'), 
    path('posts/<int:id>', views.postDetail, name='postdetail'),  
    path('<str:username>/posts', views.postList, name='allposts'),
         
]