from rest_framework import generics, permissions
from drf_fanzone.permissions import IsOwnerOrReadOnly
from .models import Supporter
from .serializers import SupporterSerializer


class SupporterList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SupporterDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
