# render() - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц и соответствующих данных.
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book ,BookInstance ,Author ,Genre  
from django.views import generic
from django.http import Http404
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

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list' #  # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения



# Данный подход является более гибким
    
# class BookListView(generic.ListView):
#   model = Book

#   def get_queryset(self):
#       return Book.objects.filter(title__icontains='war')[:5] # Получить 5 книг, содержащих 'war' в заголовке
    
    def get_context_data(self, **kwargs):
         # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context
    

class BookDetailView(generic.ListView):
    model = Book
    paginate_by = 2

      


def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
