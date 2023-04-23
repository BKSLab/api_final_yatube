from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Comment, Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @cached_property
    def _post(self):
        pk = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=pk)

    def get_queryset(self):
        return self._post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self._post,
        )

    def perform_destroy(self, instance):
        if instance.author != self._post.author:
            raise PermissionDenied(
                'Изменение чужого контента запрещено!',
            )
        super(
            CommentViewSet,
            self,
        ).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ('get', 'post')
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )
