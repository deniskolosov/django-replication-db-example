from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.settings import api_settings
from rest_framework_csv.renderers import CSVRenderer

from api.serializers import ReaderSerializer
from library.models import Reader


class PaginatedCSVRenderer(CSVRenderer):
    header = ['id', 'name', 'books.0.id', 'books.0.name']
    labels = {
        'books.0.id': 'book_id',
        'books.0.name': 'book_name',
        'id': 'reader_id',
        'name': 'reader_name',
    }
    results_field = 'results'

    def render(self, data, media_type=None, renderer_context=None, writer_opts=None):
        if not isinstance(data, list):
            data = data.get(self.results_field, [])
        return super(PaginatedCSVRenderer, self).render(data, media_type, renderer_context)


class CSVReaderInfoView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    renderer_classes = (PaginatedCSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class ReaderDetailView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
