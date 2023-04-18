from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from accounts.models import User
from .serializers import PostSerializer
from rest_framework import status
from accounts.serializers import UserSerializer


@api_view(['GET', 'PUT'])
def updatePost(request, username, id):
    try:
        post = Post.objects.get(id=id, user=User.objects.get(username=username))        
        
    except Post.DoesNotExist:
        return Response({"error": "The post is not found"}, status=404)

    if request.method == "GET":
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'You do not have permision.'})


@api_view(['DELETE'])
def deletePost(request, id, username):
    post = Post.objects.get(id=id)
    post.delete()

    return Response({'message': 'Post was deleted'})


@api_view(['GET'])
def postDetail(request, id):
    post = Post.objects.get(id=id)
    serializers = PostSerializer(post, many=False)

    return Response(serializers.data)


@api_view(['GET'])
def postList(request, username):
    posts = Post.objects.all()
    serializers = PostSerializer(posts, many=True)

    return Response(serializers.data)

@api_view(['POST'])
def createPost(request, username):
    if request.method != "POST":
        return Response({"error": "POST request required."})

    user = User.objects.get(username=username)
    title = request.data["title"]
    content = request.data['content']

    post = Post.objects.create(
        user = user,
        title = title,
        content = content,
    )

    return Response(PostSerializer(post).data)