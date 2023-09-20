from . import views
from django.urls import path



urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('contact.html', views.contact, name = 'contact'),
    path('thank_you.html', views.thank_you, name = 'thank_you'),
]
