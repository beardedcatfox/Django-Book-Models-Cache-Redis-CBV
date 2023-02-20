from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Author, Book, Publisher, Store


def index(request):
    return render(request, 'bookstore/bookstore.html')


def book_list(request):
    books = Book.objects.prefetch_related('authors', 'publisher').all()
    paginator = Paginator(books, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookstore/book_list.html', {'page_obj': page_obj})


def store_list(request):
    stores = Store.objects.prefetch_related('books').all()
    paginator = Paginator(stores, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookstore/store_list.html', {'page_obj': page_obj})


def author_list(request):
    authors = Author.objects.prefetch_related('book_set').all()
    paginator = Paginator(authors, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookstore/author_list.html', {'page_obj': page_obj})


def publisher_list(request):
    publishers = Publisher.objects.prefetch_related('book_set').all()
    paginator = Paginator(publishers, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookstore/publisher_list.html', {'page_obj': page_obj})


def author_detail(request, author_id):
    author = Author.objects.prefetch_related('book_set').get(pk=author_id)
    return render(request, 'bookstore/author_detail.html', {'author': author})


def book_detail(request, book_id):
    book = Book.objects.select_related('publisher').prefetch_related('authors').get(pk=book_id)
    return render(request, 'bookstore/book_detail.html', {'book': book})


def store_detail(request, store_id):
    store = Store.objects.prefetch_related('books').get(pk=store_id)
    return render(request, 'bookstore/store_detail.html', {'store': store})


def publisher_detail(request, publisher_id):
    publisher = Publisher.objects.prefetch_related('book_set').get(pk=publisher_id)
    return render(request, 'bookstore/publisher_detail.html', {'publisher': publisher})


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'age']
    success_url = '/authors/'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'age']
    success_url = '/authors/'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')
