from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MorhpyUserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_NOTSPECIFIED = 'N'
    GENDER_OPTIONS = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_NOTSPECIFIED, 'Not specified'),
    ]

    # Mandatory fields
    username = models.CharField(max_length=150, unique=True, help_text='Sets the first username of the user')
    email = models.EmailField(unique=True)

    # Optional Fields
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # Extra fields
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default=GENDER_NOTSPECIFIED)
    isPrivateProfile = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Social graph relationships
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')

    # Custom manager
    objects = MorhpyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.strip() or self.username
    
    def get_friend_count(self):
        return f'{self.friends.count()}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_from_user')
#     to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target_user')
#     sent_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'From: {self.from_user}, To: {self.to_user}, ats: {self.sent_at}'