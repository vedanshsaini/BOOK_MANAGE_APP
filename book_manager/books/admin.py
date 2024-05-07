from django.contrib import admin
from .models import Book, ReadingList

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'genre', 'publication_date')
    search_fields = ('title', 'authors')

@admin.register(ReadingList)
class ReadingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__username')
    filter_horizontal = ('books',)