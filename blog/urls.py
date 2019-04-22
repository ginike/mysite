from django.urls import path
from . import views
from django.conf.urls import url
from .views import PostListView, PostDetailView, PostDeleteView, PostCreateView,PostUpdateView, UserPostListView, search, search_by_anthem, search_by_classical, search_by_highlife, search_by_hymn,PostUpView, plans


urlpatterns = [
 	#path('', views.first_page, name = 'blog-first'),
    path('', PostListView.as_view(), name = 'blog-home'),    
    path('post/<int:pk>/home/', PostListView.as_view(), name = 'blog-homes'),    
    #path('result/', PostSearchListView.as_view(), name = 'blog-home'),    
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/purchase/', PostUpView.as_view(), name = 'post-purchase'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/', views.about, name = 'blog-about'),
    path('plans/', views.plans, name = 'blog-plans'),
    #path('post/<int:pk>/purchase/', PriceDetailView.as_view(), name = 'post-pricing'),
    url(r'^results/$', views.search, name="search"),
    url(r'^genre_anthem/$', views.search_by_anthem, name="anthem"),
    url(r'^genre_classical/$', views.search_by_classical, name="classical"),
    url(r'^genre_highlife/$', views.search_by_highlife, name="highlife"),
    url(r'^genre_hymn/$', views.search_by_hymn, name="hymn"),
]
