from django.contrib import admin
from catalog.models import Book
from catalog.models import BookInstance
from catalog.models import Author
from catalog.models import Genre

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Genre)

