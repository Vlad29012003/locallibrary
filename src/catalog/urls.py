from django.urls import path 
from .views import CustomLogoutView, index, BookListView, BookDetailView, AuthorListView, AuthorDetailView , LoanedBooksBylibrarianstView , LoanedBooksByUserListView , renew_book_librarian



urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', LoanedBooksBylibrarianstView.as_view(), name='all-borrowed'),
    path('book/<slug:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
]


# url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
# url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

# urlpatterns += [
#     path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
# ]
