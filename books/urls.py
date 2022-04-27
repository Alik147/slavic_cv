from . import views
from django.urls import path, reverse_lazy

app_name = 'books'
urlpatterns = [
	path('', views.BookListView.as_view(), name='all'),
	path('book/<int:pk>/update',
            views.BookUpdateView.as_view(success_url=reverse_lazy('books:all')),
            name='book_update'),
	path('book/<int:pk>/delete',
            views.BookDeleteView.as_view(success_url=reverse_lazy('books:all')),
            name='book_delete'),
      path('book/create',
           views.BookCreateView.as_view(success_url=reverse_lazy('books:all')),
           name='book_create')
]