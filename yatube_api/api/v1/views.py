from rest_framework import mixins, viewsets


class ObjectCreateAndListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
):
    pass
