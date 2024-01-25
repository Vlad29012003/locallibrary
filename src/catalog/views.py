# render() - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц и соответствующих данных.
from django.shortcuts import render
from .models import Book ,BookInstance ,Author ,Genre  
# Create your views here.

def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_book_ins = BookInstance.objects.all().count()

    # Доступные книги (статус = 'a')   
    num_instances_avalable = BookInstance.objects.filter(status='a').count()
    num_authors = Author.objects.count() # Метод 'all()' применён по умолчанию.


    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_book_ins,'num_instances_available':num_instances_avalable,'num_authors':num_authors},
    )
