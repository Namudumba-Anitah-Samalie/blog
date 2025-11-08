
from django.urls import path
from .views import base, blog, show_all, about

urlpatterns = [
    path('', base, name='base'),           # Base page
    path('blog/', blog, name='blog'),      # Blog page
    path('show_all/', show_all, name='show_all'),
    path('about/', about, name='about'),
]