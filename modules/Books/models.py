from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.Authors.models import Author
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.
GENEROS = (
    ('CF','Ciencia Ficcion'),
    ('FS','Fantasia'),
    ('TR','Terror'),
    ('IT','Tecnologia'),
    ('DR','Drama'),
)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=100)
    date_published = models.DateField()
    cover = models.URLField()
    prologue = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    literary_genre = models.CharField(choices=GENEROS, max_length=50)
    tags = ArrayField(
            models.CharField(max_length=50), blank=True, null=True
        )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Book: {0}'.format(self.title)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarista')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='libro')
    comment = models.TextField()


    def __str__(self):
        return 'Comment of user: {0} and book: {1}'.format(
                                self.author.first_name,
                                self.book.title)