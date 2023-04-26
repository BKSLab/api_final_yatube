from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property

from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.serializers import BaseSerializer

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

    def perform_create(
        self, serializer: BaseSerializer[PostSerializer],
    ) -> None:
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @cached_property
    def _post(self) -> Post:
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id'),
        )

    def get_queryset(self) -> QuerySet[Comment]:
        return self._post.comments.all()

    def perform_create(
        self, serializer: BaseSerializer[CommentSerializer],
    ) -> None:
        serializer.save(
            author=self.request.user,
            post=self._post,
        )


class FollowCreateAndListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self) -> QuerySet[Follow]:
        return self.request.user.follower.all()

    def perform_create(
        self, serializer: BaseSerializer[FollowSerializer],
    ) -> None:
        serializer.save(
            user=self.request.user,
        )
