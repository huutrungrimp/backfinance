from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status





@api_view(['GET'])
def getUser(request, id):
    user = User.objects.get(id=id)
    user_serializer = UserSerializer(user).data

    return Response(({'user': user_serializer}))



@api_view(['GET'])
def all_users(request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True).data

    return Response(({'users': users_serializer}))



@api_view(['POST'])
def userSignOut(request):
    logout(request)
    return Response(({"message": "You were logout!"}))



@api_view(['POST'])
def userSignIn(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)        
        if user is not None:
            login(request, user)
            detailUser = User.objects.get(username=username)
            serializer = UserSerializer(detailUser)
            return Response(serializer.data)
        else:
            return Response({
                "message": "Incorrect password or user name, please try again"
            })
    else:
        return Response({"message": "Please Login"})



@api_view(['POST'])
@permission_classes([AllowAny])
def userSignUp(request):
    username = request.data["username"]
    email = request.data["email"]
    password = request.data["password"]
    confirmation = request.data["password2"]
    if password != confirmation:
        return Response({"message": "Passwords must match."})
    try:
        user = User.objects.create_user(username, email, password)
        user.save()        
        return Response(UserSerializer(user).data)
    except IntegrityError:
        return Response({"message": "Username already taken."})
    

