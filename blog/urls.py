from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('api', views.blog_api, name='blog-api'),
    path('api/<int:id>', views.blog_detailed)
    
]
