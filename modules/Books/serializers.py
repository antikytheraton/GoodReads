from rest_framework import serializers
from .models import Book, GENEROS
# from modules.Authors.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):

    # author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ('')

class QuerysBookSerializer(serializers.Serializer):

    date_published = serializers.DateField(required=False)
    literary_genre = serializers.ChoiceField(choices=GENEROS, required=False)
    rating = serializers.DecimalField(max_digits=3,decimal_places=2,
                                required=False)