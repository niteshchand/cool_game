from django.urls import path
from .views import ( 
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    UserBlogListView,
    PostListView,
)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-index"),
    path('games/',views.games , name="blog-games"),
    path('blog/', BlogListView.as_view(), name="blog-blog"),
    path('quiz/', views.quiz, name="blog-quiz"),
    path('quiz1/', views.quiz1, name="blog-quiz1"),
    path('quiz2/', views.quiz2, name="blog-quiz2"),
    path('quiz3/', views.quiz3, name="blog-quiz3"),
    path('progarmquiz1/', views.progarmquiz1, name="blog-progarmquiz1"),
    path('progarmquiz2/', views.progarmquiz2, name="blog-progarmquiz2"),
    path('progarmquiz3/', views.progarmquiz3, name="blog-progarmquiz3"),
    path('about/', views.about, name="blog-about"),
    path('privacy/',views.privacy,name="blog-privacy"),
    # path('ping/', views.ping, name='blog-ping'),
    path('panda/', views.panda, name='blog-panda'),
    path('pong/', views.pong, name='blog-pong'),
    path('contact/', views.contact, name='blog-contact'),
    # path('index/',views.index,name='blog-index'),
    path('shoot/',views.shoot,name='blog-shoot'),
    path('user/<str:username>', UserBlogListView.as_view() ,name='user-blogs'),
    path('post/<int:pk>/', BlogDetailView.as_view() ,name='blog-detail'),
    path('post/new/', BlogCreateView.as_view() ,name='blog-create'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view() ,name='blog-update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view() ,name='blog-delete'),
]