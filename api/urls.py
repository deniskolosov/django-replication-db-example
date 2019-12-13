from django.urls import path

from api import views


urlpatterns = [
    path('', views.CSVReaderInfoView.as_view(), name='csv-export'),
    path('readers/<int:pk>/', views.ReaderDetailView.as_view(), name='readers-detail'),
]
