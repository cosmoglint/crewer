from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from ProjectManager.permissions import IsManager
from rest_framework import generics
from django.http import Http404
from django.conf import settings
from .serializers import RegisterUserSerializer, UserSerializer, ManageUserSerializer
from .permissions import IsOwnerOrManager

from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(APIView):
    '''
    Lists down all users
    '''
    permission_classes = [permissions.IsAuthenticated, IsManager]
    def get(self, request):
        users = User.objects.all()
        serializer = ManageUserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

class UserProfileView(APIView):
    '''
    Shows the current user\'s profile to themselves
    '''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        current_user = request.user
        serializer = UserSerializer(current_user, context={'request': request})
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    '''
    Detailed view selected user profile
    '''
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrManager]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        if request.user.is_manager():
            serializer = ManageUserSerializer(user)
        else:
            serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        if request.user.is_manager():
            serializer = ManageUserSerializer(user, data=request.data)
        else:
            serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    '''
    Detailed view selected user profile
    '''
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterUserSerializer
