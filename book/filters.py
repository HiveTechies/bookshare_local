from .models import Book,Chapter
import django_filters

class BookFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Book
        fields = {
            # 'name':['icontains'],
        }

    
class ChapterFilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = Chapter
        fields = {
            # 'name':['icontains'],
        }

