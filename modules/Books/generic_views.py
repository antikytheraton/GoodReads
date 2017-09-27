from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class ListBook(generics.ListCreateAPIView):
    # GET Y POST
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('rating','date_published','price','literary_genre')
    search_fields = ('title','prologue','literary_genre')
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     pass
    # def List(self, request, *args, **kwargs):
    #     pass
    # def Create(self, request, *args, **kwargs):
    #     pass

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    # GET, PUT, DELETE Y PATCH
    serializer_class = BookSerializer
    queryset = Book.objects.all()