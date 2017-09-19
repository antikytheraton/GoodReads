from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookSerializer, QuerysBookSerializer
from .models import Book
from django.http import Http404
from django.db.models import Q

# Create your views here.
class ListBook(APIView):

    def get(self, request):
        if request.query_params:
            queryparam = QuerysBookSerializer(data=request.query_params)
            if queryparam.is_valid():
                data = queryparam.validated_data
                books = Book.objects.filter(**data)
                serializer = BookSerializer(books,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(queryparam.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailBook(APIView):

    def _getBook(self, pk):
        try:
            return Book.objects.get(pk=pk)
            '''
                SELECT * FROM BOOK WHERE id=PK
            '''
        except:
            raise Http404

    def get(self, request, pk):
        book = self._getBook(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = self._getBook(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self._getBook(pk)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        book = self._getBook(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)