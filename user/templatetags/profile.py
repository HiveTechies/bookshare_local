from django import template
register = template.Library()
from django.template import loader
from book.models import Book
from django.contrib.auth.models import User

@register.simple_tag(takes_context=True)
def total_reads(context,id):
    request = context['request']
    view_count=0
    author=User.objects.get(id=id)
    books=Book.objects.filter(author=author)
    for book in books:
       view_count+= book.hit_count.hits
    return view_count


@register.simple_tag(takes_context=True)
def published_books(context,id):
    request = context['request']
    author=User.objects.get(id=id)
    published_books=Book.objects.filter(author=author)
    return loader.get_template('user/books.html').render({
        'books':published_books,
    })