from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # regex version
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]