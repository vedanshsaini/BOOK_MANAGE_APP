from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    def delete_book(self):
        self.delete()

class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_lists')
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='reading_lists')

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name