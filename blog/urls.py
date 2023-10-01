from . import views
from django.urls import path
from .views import AddPost



urlpatterns = [
    path('update_post/<slug:slug>/', views.UpdatePost.as_view(), name= 'update_post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('contact/', views.contact, name = 'contact'),
    path('thank_you/', views.thank_you, name = 'thank_you'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('', views.PostList.as_view(), name='blog'),
]
