from django import template
register = template.Library()
from django.template import loader
from book.models import Book

@register.simple_tag(takes_context=True)
def total_reads(context):
    request = context['request']
    view_count=0
    books=Book.objects.filter(author=request.user)
    for book in books:
       view_count+= book.hit_count.hits
    return view_count


@register.simple_tag(takes_context=True)
def published_books(context):
    request = context['request']
    published_books=Book.objects.filter(author=request.user)
    return loader.get_template('user/books.html').render({
        'books':published_books,
    })

@register.simple_tag(takes_context=True)
def drafted_books(context):
    request=context['request']
    drafted_books=Book.objects.filter(author=request.user, author_status='D')
    return loader.get_template('user/books.html').render({
        'books':drafted_books,
    })


@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name='Author').exists() 