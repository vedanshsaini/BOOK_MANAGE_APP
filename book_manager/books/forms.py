from django import forms
from .models import Book
from .models import ReadingList

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'genre', 'publication_date', 'description']


class ReadingListForm(forms.ModelForm):
    class Meta:
        model = ReadingList
        fields = ['name']
