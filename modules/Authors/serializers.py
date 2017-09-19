from rest_framework import serializers
from .models import Author
from modules.Books.serializers import BookSerializer

def name_only_aaron(source):
    if source == "Aaron" or "aaron":
        pass
    else:
        raise serializers.ValidationError("No te llamas Aaron")
class ExampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,validators=[name_only_aaron])
    last_name = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    age = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ('is_alive',)
