from django.urls import path


from audiobook.views.get_books import get_books 
from audiobook.views.upload_book import upload_book
from audiobook.views.get_book import get_book

urlpatterns = [
    path('get-books/',get_books,name="get-books"),
    path('get-book/',get_book,name="get-book"),
    path('upload-book/',upload_book,name="upload-book")
]
