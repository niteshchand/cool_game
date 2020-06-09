from django.shortcuts import render , get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView ,
     DetailView ,
      CreateView,
      UpdateView ,
      DeleteView,
      
)
from .models import Post
from .models import Blog


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'blogs'
    # ordering = ['-date_posted']
    # paginate_by = 5

class UserBlogListView(ListView):
    model = Blog
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'blogs'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user).order_by('-date_posted')


class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin , CreateView):
    model = Blog
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin ,UserPassesTestMixin , UpdateView):
    model = Blog
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Blog
    success_url = '/'
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


def games(request):
    return render(request,'blog/games.html', {'title':'games'})



def quiz(request):
    return render(request,'blog/quiz.html', {'title':'quiz'})

def quiz1(request):
    return render(request,'blog/quiz1.html', {'title':'quiz1'})

def quiz2(request):
    return render(request,'blog/quiz2.html', {'title':'quiz2'})

def quiz3(request):
    return render(request,'blog/quiz3.html', {'title':'quiz3'})

def progarmquiz1(request):
    return render(request,'blog/progarmquiz1.html',{'title':'progarmquiz1'})

def progarmquiz2(request):
    return render(request,'blog/progarmquiz2.html',{'title':'progarmquiz2'})

def progarmquiz3(request):
    return render(request,'blog/progarmquiz3.html',{'title':'progarmquiz3'})

def about(request):
    return render(request,'blog/about.html', {'title':'about'})

def contact(request):
    return render(request,'blog/contact.html', {'title':'contact'})

def privacy(request):
    return render(request,'blog/privacy.html',{'title':'privacy'})

def panda(request):
    return render(request,'blog/panda.html',{'title':'panda'})

def pong(request):
    return render(request,'blog/pong.html',{'title':'pong'})

def shoot(request):
    return render(request,'blog/shoot.html',{'title':'shoot'})