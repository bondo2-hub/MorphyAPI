from rest_framework import mixins, generics, viewsets, status, exceptions
from rest_framework.response import Response
from .serializers import *
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserListSerializer

class UserFriendsViewSet(viewsets.ModelViewSet):

    def create(self, request, user_pk=None):
        user = User.objects.filter(pk=user_pk).first()
        if not user:
            return Response({"detail": "Target user not found."}, status=404)

        serializer = AddFriendToUserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": f"Friend added to {user.username}."}, status=201)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddFriendToUserSerializer
        return UserFriendListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        try:
            user = User.objects.get(pk=user_id)
            return user.friends.all()
        except User.DoesNotExist:
            raise exceptions.NotFound(detail="No user found with the given ID/PK")
        
class UserChatroomViewSet(viewsets.ModelViewSet):
    serializer_class = UserChatroomListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise exceptions.NotFound('User not found.')
        return Chatroom.objects.filter(members=user)