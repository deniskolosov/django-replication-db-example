from django.test import TestCase, Client

from rest_framework.reverse import reverse

from library.factories import ReaderFactory, BookFactory, BookReaderFactory


class GetReaderTestCase(TestCase):
    def setUp(self):
        self.reader = ReaderFactory(name='John Doe')
        self.book = BookFactory(name='Ulysses')
        self.book_reader = BookReaderFactory(book=self.book, reader=self.reader)
        self.url = reverse('readers-detail', args=[self.reader.pk])
        self.client = Client()
        self.expected_response = {'id': self.reader.pk, 'name': 'John Doe',
                                  'books': [{'id': self.book.pk, 'name': 'Ulysses'}]}

    def test_get_reader_with_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertEqual(results, self.expected_response)


class GetCSVTestCase(TestCase):
    def setUp(self):
        self.reader = ReaderFactory(name='John Doe')
        self.book = BookFactory(name='Ulysses')
        self.book_reader = BookReaderFactory(book=self.book, reader=self.reader)
        self.url = reverse('csv-export')
        self.expected_response = b'reader_id,reader_name,book_id,book_name\r\n%b,John Doe,%b,Ulysses\r\n' % (
            str(self.reader.pk).encode(), str(self.book.pk).encode())

    def test_get_all_readers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, self.expected_response)
