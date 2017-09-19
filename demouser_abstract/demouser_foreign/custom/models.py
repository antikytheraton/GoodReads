from django.db import models
from django.contrib.auth.models import User

class Alumni(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cinta = models.CharField(max_length=100)
# Create your models here.
