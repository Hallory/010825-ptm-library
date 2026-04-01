from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers.book import BookSerializer


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = Book.objects.all()
        
        year_from = self.request.query_params.get('year_from')
        category_name = self.request.query_params.get('category_name')
        
        if year_from:
            queryset = queryset.filter(published_date__year__gte=year_from)
            
        if category_name:
            queryset = queryset.filter(category__name=category_name)
            
        return queryset 