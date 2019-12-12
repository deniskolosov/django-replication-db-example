from io import StringIO

from django.core.management import call_command
from django.db.models import Q
from django.test import TestCase

from library.models import Book, Reader


class GenerateDataCommandTestCase(TestCase):

    def test_data_generated(self):
        out = StringIO()
        initial_books_count = Book.objects.count()
        initial_readers_count = Reader.objects.count()
        initial_readers_with_books_count = Reader.objects.filter(~Q(books=None))
        call_command('generate_data', books=3, readers=3, readers_with_books=3, stdout=out)
        current_books_count = Book.objects.count()
        current_readers_count = Reader.objects.count()
        current_readers_with_books_count = Reader.objects.filter(~Q(books=None)).count()

        # Additional books are created with readers_with_books option, so 3+3
        self.assertEqual(current_books_count, initial_books_count+6)
        self.assertEqual(current_readers_count, initial_readers_count+6)
        self.assertEqual(current_readers_with_books_count, 3)
        self.assertIn('{} books was created'.format(3), out.getvalue())
        self.assertIn('{} readers was created'.format(3), out.getvalue())
        self.assertIn('{} readers with books was created'.format(3), out.getvalue())
