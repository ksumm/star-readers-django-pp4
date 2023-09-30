from . import views
from django.urls import path
from .views import AddPost



urlpatterns = [
    path('add_post.html', views.AddPost.as_view(), name='add_post'),
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('contact.html', views.contact, name = 'contact'),
    path('thank_you.html', views.thank_you, name = 'thank_you'),
]
