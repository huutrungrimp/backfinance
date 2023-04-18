from django.urls import path
from django.conf.urls import include
from django.urls import path
from . import views



app_name = 'accounts'
urlpatterns = [  
    path('', include('rest_auth.urls')),
    path('users/<int:id>', views.getUser),
    path('users', views.all_users),
    path('signup', views.userSignUp),
    path('signin', views.userSignIn),
    path('signout', views.userSignOut),
]
