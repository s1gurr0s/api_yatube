from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_pk>\d+)/comments',
    CommentViewSet, basename='posts_comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]