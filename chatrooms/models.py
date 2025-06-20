from django.db import models
from core.models import User
from django.core.exceptions import ValidationError

class Chatroom(models.Model):
    DM = 'DM'
    GROUP = 'GROUP'
    CHAT_TYPE_CHOICES = [
        (DM, 'Direct Message'),
        (GROUP, 'Group Chat'),
    ]

    members = models.ManyToManyField(User, related_name='chatrooms')
    chat_type = models.CharField(max_length=10, choices=CHAT_TYPE_CHOICES, default=GROUP)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_type} Chatroom {self.id} with {self.members.count()} member(s)"

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_authored')
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f"Message by {self.author} at {self.sent_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        ordering = ['-sent_at']