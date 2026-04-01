from django.urls import path

from library.views.books import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
]