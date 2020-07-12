from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import PostFilter
from .forms import *

from tracking_analyzer.models import Tracker
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from taggit.models import Tag




def home(request):
   #Querying required data
    post_list = Post.objects.all().order_by('-date_posted')
    post_filter = PostFilter(request.GET, queryset=post_list)

    paginator =Paginator(post_filter.qs,10)
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
        "posts":queryset,
        "page_request_var":page_request_var,
        'post_filter':post_filter,
    }
    return render(request, 'blog/home.html', context)


# DEPRECATED LIST VIEW (CURRENT LIST VIEW IS -> HOME VIEW)
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=Post

@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,user=request.user)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('blog-home')
    else:
        post_form = PostForm(user=request.user)
        context = {'form':post_form}
        return render(request,'blog/post_form.html',context=context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class TagPostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs.get("tagname"))
        return Post.objects.filter(tags=tag)