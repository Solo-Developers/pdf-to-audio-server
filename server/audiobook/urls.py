from django.urls import path


from audiobook.views.get_books import get_books
urlpatterns = [
    path('get-books/',get_books,name="get-books")
]
