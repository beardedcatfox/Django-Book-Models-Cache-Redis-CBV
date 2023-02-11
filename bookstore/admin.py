from django.contrib import admin

from .models import Author, Book, Publisher, Store


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
    search_fields = ['name']
    list_filter = ['name', 'age']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    list_filter = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'publisher_name', 'pubdate', 'get_authors')
    filter_horizontal = ('authors',)
    search_fields = ['name', 'publisher__name']
    list_filter = ['rating', 'pubdate', 'price', 'pages']

    def publisher_name(self, obj):
        return obj.publisher.name
    publisher_name.short_description = 'Publisher'

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('publisher').prefetch_related('authors')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_books')
    search_fields = ['name']
    list_filter = ['name']

    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('books')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Store, StoreAdmin)
