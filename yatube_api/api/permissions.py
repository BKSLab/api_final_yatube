from django.http import HttpRequest

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.views import APIView


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(
        self,
        request: HttpRequest,
        view: APIView,
        obj: object,
    ) -> bool:
        del view
        return request.method in SAFE_METHODS or obj.author == request.user
