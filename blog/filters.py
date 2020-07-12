from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Post
        fields = {
            # 'name':['icontains'],
        }
