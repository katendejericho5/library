from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    student_number = models.CharField(max_length=20)
    
from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

STATUS_CHOICES =(
    ('available for borrowing','Available for borrowing'),
    ('not available','Not Available'),
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200 ,default="Enter Author's name")
    DESCRIPTION = models.CharField(max_length=200 ,default="Enter Description")
    GENRE = models.CharField(max_length=200 ,default="Enter Genre")
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books" #optional parameter
    )
    status= models.CharField(
        max_length=150,
        choices=STATUS_CHOICES
    )
    def __str__(self):
        return self.title

# books/models.py


# Inside your Book class.
def get_absolute_url(self):
    return reverse("book_detail", kwargs={"pk": self.id})
