from django.conf.urls import url
from django.urls import path, re_path
from django.views.static import serve

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('users/<slug:category_name>/', views.users, name='users'),
    path('<slug:category_name>/', views.category_name, name='category_name'),
    path('<slug:category_name>/<slug:son_category>', views.son_category, name='category_name'),
    path('<slug:category_slug>/<slug:son_category_slug>/<int:id>', views.article, name='category_name'),

]

