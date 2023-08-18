from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django import forms


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.PositiveIntegerField()
    categories = models.CharField(max_length=200, blank=False)
    thumbnail_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False)  # Associated with a valid Book instance
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)  # Associated with a valid User instance
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Between 1 and 5
    review_text = models.TextField(blank=False, validators=[MinLengthValidator(10)])  # Minimum length of 10 characters

    class Meta:
        unique_together = [['book', 'user']]
        ordering = ['-rating']

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description', 'page_count', 'categories', 'thumbnail_url']