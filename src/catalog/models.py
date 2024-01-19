from typing import Any
from django.db import models
from django.urls import reverse
import uuid

# моделька жанра 
class Genre(models.Model):
    name = models.CharField(max_length = 200, help_text ='Enter a book genre (e.g. Science Fiction, French Poetry etc.)')

#  предназначен для предоставления строкового представления объекта.
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    


# Прмер модельки созлает обьект но не добавляет в базу данных но используются для других частях приложения 
# class SimpleModel:
#     def __init__(self, name):
#         self.name = name
    

# Моделька книги 
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author',on_delete= models.SET_NULL, null = True)
    summary = models.TextField(max_length = 1000, help_text ="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length = 100, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre',help_text ='Select a genre for this book')

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail',args=[str(self.id)])
    
# Модель экземпляра книги 
class BookInstance(models.Model):
    # используется для поля id, чтобы установить его как primary_key для этой модели. Этот тип поля выделяет глобальное уникальное значение для каждого экземпляра (по одному для каждой книги, которую вы можете найти в библиотеке).
    id = models.UUIDField(primary_key =True, default = uuid.uuid4, help_text ='Unique ID for this particular book across whole library' )
    book = models.ForeignKey('Book', on_delete = models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null = True , blank=True)

# Статусы книги 
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On load'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status = models.CharField(max_length =1 , choices=LOAN_STATUS , blank =True, default ='m', help_text = 'Book availability')

    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return '%s (%s)' % (self.id , self.book.title)
    
# Модель Автор 
class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField(null=True , blank=True)
    date_of_death = models.DateField('Died',null = True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return '%s , %s' % (self.first_name , self.last_name) 
    
    
