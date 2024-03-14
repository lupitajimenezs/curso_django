from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # PODEMOS lIMITAR LAS OPCIONES
    http_method_names = ["get"]

#USANDO PostViewSet
# class PostViewSet(ViewSet):

#     def list(self, request):
#         post = PostSerializer(
#             Post.objects.all(),
#             many = True
#         )
#         return Response(
#             status=status.HTTP_200_OK,
#             data=post.data
#         )
    
#     def retrieve(
#         self,
#         request,
#         pk : int
#     ):
#         post = PostSerializer(Post.objects.get(pk = pk))
#         return Response(
#             status = status.HTTP_200_OK,
#             data= post.data
#         )

#     def create(self, request):
#        post = PostSerializer(data = request.POST)
#        post.is_valid(raise_exception = True)
#        post.save()

#        return Response(
#            status = status.HTTP_200_OK,
#            data = post.data
#         )
    

#Usando el APIView
# class PostApiView(APIView):

#     def get(self, request):
#         post = PostSerializer(
#             Post.objects.all(),
#             many = True
#         )
#         return Response(
#             status=status.HTTP_200_OK,
#             data=post.data
#         )

#     def post(self, request):
#        post = PostSerializer(data = request.POST)
#        post.is_valid(raise_exception = True)
#        post.save()

#        return Response(
#            status = status.HTTP_200_OK,
#            data = post.data
#         )