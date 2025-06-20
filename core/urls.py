from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

users_router = routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('friends', views.UserFriendsViewSet, basename='user-friends')
users_router.register('chatrooms', views.UserChatroomViewSet, basename='user-chatrooms')

urlpatterns = [] + router.urls + users_router.urls