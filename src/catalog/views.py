# render() - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц и соответствующих данных.
from django.shortcuts import render
from .models import Book ,BookInstance ,Author 
from django.views import generic
from django.http import Http404


def index(request):
    num_books = Book.objects.all().count()
    num_book_ins = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_authors = Author.objects.count()

    all_books = Book.objects.all()  # Получаем все книги

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_book_ins,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'all_books': all_books,  # Передаем список всех книг в контекст
        },
    )
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
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
