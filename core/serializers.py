from rest_framework import serializers
from .models import *
from chatrooms.models import *

class UserFriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'gender', 'is_active']
      
class UserListSerializer(serializers.ModelSerializer):
    friends = UserFriendListSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'birth_date', 'friends', 'gender', 'isPrivateProfile', 'is_active']

class AddFriendToUserSerializer(serializers.Serializer):
    target_userID = serializers.IntegerField(required=True)

    def validate(self, data):
        try:
            friend = User.objects.get(pk=data['target_userID'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found with the given ID.")

        if self.instance and self.instance.id == friend.id:
            raise serializers.ValidationError("You cannot add yourself as a friend.")

        data['friend'] = friend
        return data

    def update(self, instance, validated_data):
        friend = validated_data['friend']
        instance.friends.add(friend)
        return instance

    def create(self, validated_data):
        return self.update(self.instance, validated_data)

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'gender', 'phone_number']

class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UserChatroomListSerializer(serializers.ModelSerializer):
    members = UserSummarySerializer(many=True)

    class Meta:
        model = Chatroom
        fields = ['id' ,'members', 'chat_type', 'created_at']
