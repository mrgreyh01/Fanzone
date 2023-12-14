from rest_framework import generics, permissions
from drf_fanzone.permissions import IsOwnerOrReadOnly
from .models import Support
from .serializers import SupporterSerializer


class SupporterList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Support.objects.all()
    serializer_class = SupporterSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SupporterDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Support.objects.all()
    serializer_class = SupporterSerializer
