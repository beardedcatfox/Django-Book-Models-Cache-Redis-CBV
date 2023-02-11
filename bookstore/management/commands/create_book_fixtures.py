import random

from bookstore.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Generate fake fixtures for the Author, Publisher, Book, and Store models'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of fixtures to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for i in range(total):
            author = Author.objects.create(
                name=fake.name(),
                age=random.randint(20, 80)
            )
            publisher = Publisher.objects.create(
                name=fake.company()
            )
            book = Book.objects.create(
                name=fake.catch_phrase(),
                pages=random.randint(100, 500),
                price=random.uniform(5.00, 50.00),
                rating=float('{:.1f}'.format(random.uniform(1.0, 5.0))),
                publisher=publisher,
                pubdate=fake.date_between(start_date='-30y', end_date='today'),
            )
            book.authors.add(author)
            store = Store.objects.create(
                name=fake.company()
            )
            store.books.add(book)

        self.stdout.write(self.style.SUCCESS(f'{total} fixtures created successfully'))
