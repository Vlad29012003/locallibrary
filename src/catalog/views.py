# render() - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц и соответствующих данных.
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book ,BookInstance ,Author 
from django.views import generic
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin # LoginRequiredMixin в Django - это класс-миксин, который добавляет требование аутентификации пользователя к представлению.
# Если пользователь не вошел в систему, он будет перенаправлен на страницу входа, прежде чем получить доступ к защищенному представлению.


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


def index(request):
    num_books = Book.objects.all().count()
    num_book_ins = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()
    # 'all()' подразумевается по умолчанию.
    num_authors = Author.objects.count()

# Количество посещений этого представления, подсчитанное в переменной сеанса.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    all_books = Book.objects.all()  # Получаем все книги


    # Отображение HTML-шаблона index.html с данными в переменной контекста.
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_book_ins,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_visits':num_visits,
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
    

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 5

      
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



class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'authors/author_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Author.objects.all().order_by('last_name', 'first_name')


    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        return context
    

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 3
    template_name = 'authors/author_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        try:
            author = Author.objects.get(pk=pk)
            return author
        except Author.DoesNotExist:
            raise Http404('Author does not exist')
        


