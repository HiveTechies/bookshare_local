from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book, Genre, Chapter

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse

# from user.models import Read
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from user.models import Collection
from .forms import *

from .filters import BookFilter, ChapterFilter

from taggit.models import Tag
from .forms import BookForm

from termsandconditions.decorators import terms_required
from django.forms import ModelForm, Textarea
from tracking_analyzer.models import Tracker


@terms_required
def all_books(request):
    #Querying required data
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    
    query_list=book_filter.qs
    #Paginating books result
    paginator =Paginator(query_list,12)
    page_request_var="page"
    page=request.GET.get(page_request_var)
    try:
        queryset=paginator.get_page(page)
    except PageNotAnInteger:
        queryset=paginator.get_page(1)
    except EmptyPage:
        queryset=paginator.get_page(paginator.num_pages)

    #Sending data to page
    context={
        "books":queryset,
        "page_request_var":page_request_var,
        'book_filter': book_filter,
    }
    #returns home page in books
    return render(request, 'book/allbooks.html', context)


# Genre function to retrieve genres
def genre(request):
    query_list = Genre.objects.all()
    context = {
        "genres": query_list,
    }
    return render(request, "book/genre.html", context)


class BookCreateView(CreateView):
    model = Book
    fields=['name','about','image','genre','published_date','tags','lang_code','is_explicit','pages']
    widgets = {
            'about': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    def get_form(self):
        '''add date picker in forms'''
        from django.forms.widgets import SelectDateWidget
        form = super(BookCreateView, self).get_form()
        form.fields['published_date'].widget = SelectDateWidget()
        return form
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

@login_required
def create_chapter(request):
    if request.method == 'POST':
        chapter_form = ChapterCreateForm(request.POST,user=request.user)
        if chapter_form.is_valid():
            chapter_form.instance.author = request.user
            chapter_form.save()
            messages.success(request,f'Your Chapter is now live on Zoro!')
            return redirect('home')
    else:
        chapter_form = ChapterCreateForm(user=request.user)
    context = {
        'chapter_form':chapter_form
    }
    return render(request,'book/chapter_form.html',context)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ["name", "genre", "image", "lang_code", "author","is_explicit"]

    def form_valid(self, form):
        form.instance.author= self.request.user
        form.save()
        return super().form_valid(form)


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    model = Chapter
    fields = ["book", "name", "content"]

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GenreBookListView(ListView):
    model = Book
    template_name = "book/allbooks.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        genre = get_object_or_404(Genre, genre=self.kwargs.get("genrename"))
        return Book.objects.filter(genre=genre)


# Shows detail view of book
def book_detail_view(request, book_id):
    # FETCH BOOK WITH ID FROM USER
    book = get_object_or_404(Book, id=book_id)

    # Track object starts here
    Tracker.objects.create_from_request(request, book)
    # Track object ends here

    # LOGIC
    hit_counts=book.hit_count.hits
    hit_count = HitCount.objects.get_for_object(book)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    chapters=book.chapters.all()
    chapter_filter = ChapterFilter(request.GET, queryset=chapters)
    chapters=chapter_filter.qs

    # PREPARE DATA FOR SENDING
    context={
        'book': book,
        'chapters':chapters,
        'chapter_filter':chapter_filter,
    }
    return render(request, "book/book_detail.html", context)


class ChapterDetailView(DetailView):
    model = Chapter


@login_required
def favorite(request):
    user = request.user
    books = user.favorite.all()
    context = {
        "books": books,
        'message': 'Favorites'
    }
    return render(request, "book/allbooks.html", context=context)


@login_required
def add_favorite(request):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    Tracker.objects.create_from_request(request, book)
    if book.favorite.filter(id=request.user.id).exists():
        book.favorite.remove(request.user)
    else:
        book.favorite.add(request.user)
    return HttpResponse('')


@login_required
def collection(request):
    collections = Collection.objects.filter(user=request.user.id)
    context = {
        "collections": collections,
        'message': 'Collections'
    }
    return render(request, "book/collection.html", context)

@login_required
def create_collection(request):
    if request.method=='POST':
        name=request.POST['collection']
        if Collection.objects.filter(name=name).exists():
            return HttpResponse('exists')
        else:
            Collection.objects.create(
                name=name,
                user=request.user
            )
            book_id = str(request.POST['bookid'])
            # Get book object using ID
            book=get_object_or_404(Book, id=int(book_id))
            created=Collection.objects.get(name=name)
            # Adding book to created_collection
            created.books.add(book)
            # sending html data
            send=f'''<input type="checkbox" class="collection" name=" ''' + str(created.id) +''' " id="collection''' +str(created.id)+''' "  book_id="+''' +book_id+'''" collection_id=" '''+str(created.id)+''' "checked><label>&nbsp;&nbsp;'''+created.name+'''</label></input> <br>''' 
            print(send)
            return HttpResponse(send)

@login_required
def add_book_to_collection(request):
    # Getting book from POST[book_id]   
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    collection = get_object_or_404(Collection, id=request.POST.get('collection_id'))
    data=''
    if collection.books.filter(id=book.id).exists():
        collection.books.remove(book)
        data='r'
        return HttpResponse(data)
    else:
        collection.books.add(book)
        data='a'
        return HttpResponse(data)   


@login_required
def books_in_collection(request, collection_id):
    coll = get_object_or_404(Collection, id=collection_id)
    collections = Collection.objects.filter(user=request.user.id)
    books = coll.books.all()
    paginator = Paginator(books, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        query = paginator.get_page(page)
    except PageNotAnInteger:
        query = paginator.get_page(1)
    except EmptyPage:
        query = paginator.get_page(paginator.num_pages)

    context = {
        "books": query,
        "page_request_var": page_request_var,
        "message": 'Collection - '+coll.name,
    }
    return render(request, "book/allbooks.html", context=context)

class TagBookListView(ListView):
    model = Book
    template_name = "book/allbooks.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs.get("tagname"))
        return Book.objects.filter(tags=tag)


class GenreCreateView(CreateView):
    model = Genre
    fields = ['genre']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)