from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from . import models
from . import forms

# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    template = 'books/book_list.html'
    model = models.Book


class BookCreateView(LoginRequiredMixin, CreateView):
    template = 'books/book_form.html'
    model = models.Book
    form_class = forms.BookForm
    

class BookDeleteView(LoginRequiredMixin, DeleteView):
    template = 'books/book_confirm_delete.html'
    model = models.Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template = 'books/book_form.html'
    model = models.Book
    form_class = forms.BookForm