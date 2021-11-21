from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .serializers import FileSerializer
from .models import File
from rest_framework import permissions
class FileList(ListCreateAPIView):

    serializer_class = FileSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

class FileDetaiView(RetrieveUpdateDestroyAPIView):
    serializer_class = FileSerializer

    permission_classes = (permissions.IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)
