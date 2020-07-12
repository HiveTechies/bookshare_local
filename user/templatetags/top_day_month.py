from django import template
register = template.Library()
from django.template import loader
from book.models import Book


books=Book.objects.all()

def top(days):
    top_day=list()
    for book in books:
        top_day.append(book.hit_count.hits_in_last(days=days))
    yx=zip(top_day, books)
    top_day= [x for y, x in yx]
    return top_day[:10]


@register.simple_tag(takes_context=True)
def top_day(context):
    top_day=top(1)
    return loader.get_template('user/books.html').render({
        'books': top_day
    })

@register.simple_tag(takes_context=True)
def top_week(context):
    top_week=top(7)
    return loader.get_template('user/books.html').render({
        'books': top_week,
    })

@register.simple_tag(takes_context=True)
def top_month(context):
    top_month=top(30)
    return loader.get_template('user/books.html').render({
        'books': top_month,
    })
