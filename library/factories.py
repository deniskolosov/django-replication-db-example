import factory

from library.models import Book, Reader, BooksReaders


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book
    name = factory.Sequence(lambda n: 'Story %s' % n)


class ReaderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Reader

    name = factory.Sequence(lambda n: 'John Doe %s' % n)


class BookReaderFactory(factory.DjangoModelFactory):
    class Meta:
        model = BooksReaders
    book = factory.SubFactory(BookFactory)
    reader = factory.SubFactory(ReaderFactory)


class ReaderWithBooksFactory(ReaderFactory):
    book_reader_link = factory.RelatedFactory(BookReaderFactory, 'reader')
