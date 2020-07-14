from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileUpdateForm, DeveloperRegistrationForm, ReportForm
from django.contrib.auth.decorators import login_required
from book.models import Book
from .models import Collection, Profile, ExplicitReport
from django.contrib.auth.models import User
from book.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from friendship.models import Friend, Follow, Block
from .filters import UserFilter
from termsandconditions.decorators import terms_required
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.timezone import utc
import datetime
import random
from django.db.models import Max
from friendship.models import Friend, Follow, Block



books=Book.objects.all()

# SITE HOME PAGE
def home(request):
    updated_books = books.order_by('-id')[:12]
    max_id = Book.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    book = Book.objects.filter(pk=pk).first()

    context = {
        'random_book':book,
        'row1': updated_books[:4],
        'row2':updated_books[4:8],
        'row3': updated_books[8:12],
    }
    return render(request, 'user/home.html', context)

# TRENDING PAGE
def trending(request):
    trending_books = books.order_by('-hit_count_generic__hits')[:27]
    paginator =Paginator(trending_books,9)
    page_request_var="page"
    page=request.GET.get(page_request_var)
    try:
        queryset=paginator.get_page(page)
    except PageNotAnInteger:
        queryset=paginator.get_page(1)
    except EmptyPage:
        queryset=paginator.get_page(paginator.num_pages)
    context = {
        'books': queryset,
        "page_request_var":page_request_var,
        'message': 'Trending',
    }
    return render(request, 'book/allbooks.html', context)


def view_profile(request,username):
    user=User.objects.get(username=username)
    if request.user.is_authenticated:
        following = Follow.objects.following(request.user)
    else:
        following=None
    print(following)
    return render(request,'user/view_profile.html',{'user':user, 'following': following})


def user_profile(request,user_id):
    user=User.objects.get(pk=user_id)
    return render(request,'user/user_profile.html',{'user':user})

def user_search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user/user_search.html', {'users': user_filter})

def studio(request):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    timediff = now - request.user.last_login
    days= timediff.total_seconds()/60/60/24
    if days>4:
        messages.success(
            request,f'Welcome back creator! We placed everything ready for you to create wonders'
        )
    return render(request,'user/studio.html')

def view_user_profile(request, user_id):
    return render(request, 'user/profile.html')


def handler404(request, exception):
    response = render("user/404.html")
    response.status_code = 404
    return response


def handler500(request):
    response = render('user/500.html')
    response.status_code = 500
    return response

def following(request):
    return render(request, 'user/following.html')


def add_or_remove_follow(request):
    user_id=request.POST['follower_id']
    user=User.objects.get(id=user_id)
    action=request.POST['action']
    if action=='f':
        Follow.objects.add_follower(request.user, user)
        return HttpResponse('u')
    else:
        Follow.objects.remove_follower(request.user, user)
        return HttpResponse('f')

def report(request):
    if request.method == 'POST':
        form =ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_thanks')
    else:
        form = ReportForm()
    return render(request, 'user/report_form.html', {'form': form})

def report_thanks(request):
    return render(request, 'user/report_thanks.html')


#DEVELOPER VIEWS

def dev_home(request):
    if request.method == 'POST':
        form = DeveloperRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dev_thanks')
    else:
        form = DeveloperRegistrationForm()
    return render(request, 'user/dev_form.html', {'form': form})


def dev_thanks(request):
    return render(request, 'user/dev_thanks.html')

def opensource(request):
    return render(request, 'user/opensource.html')
