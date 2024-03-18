from django.urls import include, path , re_path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    re_path(r'books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
]

urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail')

]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed')
]


urlpatterns += [
    path('accounts/',  include('django.contrib.auth.urls')),
]


urlpatterns += [
    path('logout', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]
# url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
# url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

# urlpatterns += [
#     path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
# ]
