import sys

from django.core.management import BaseCommand, CommandError

from library.factories import BookFactory, ReaderFactory, BookReaderFactory, ReaderWithBooksFactory
from library.models import Reader, BooksReaders, Book


class Command(BaseCommand):
    help = 'Creates specified number of books, readers and book-reader links.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--books',
            type=int,
            help='Number of books to be added.'
        )
        parser.add_argument(
            '--readers',
            type=int,
            help='Number of readers to be added.'
        )
        parser.add_argument(
            '--readers_with_books',
            type=int,
            help='Create links between readers and books'
        )

    def handle(self, *args, **options):
        """
        Generate books, readers and book-reader links.
        """
        # Don't generate if it's already there.
        if Book.objects.all() or Reader.objects.all() or BooksReaders.objects.all():
            self.stdout.write(
                'Data exists, not generating')
            sys.exit()

        if options['books']:
            try:
                BookFactory.create_batch(options['books'])
                self.stdout.write(self.style.SUCCESS('{} books was created '.format(options['books'])))
            except Exception as e:
                raise CommandError('Something went wrong: {}'.format(repr(e)))

        if options['readers']:
            try:
                ReaderFactory.create_batch(options['readers'])
                self.stdout.write(self.style.SUCCESS('{} readers was created'.format(options['readers'])))
            except Exception as e:
                raise CommandError('Something went wrong: {}'.format(repr(e)))

        if options['readers_with_books']:
            try:
                ReaderWithBooksFactory.create_batch(options['readers_with_books'])
                self.stdout.write(self.style.SUCCESS(
                    '{} readers with books was created'.format(options['readers_with_books'])))
            except Exception as e:
                raise CommandError('Something went wrong: {}'.format(repr(e)))
