from operator import mod
from django.urls import path
from books.views import views
from books.views.modelview import AuthorViewSet, BookViewSet

urlpatterns = [
    path('books/', views.RetrieveBooks.as_view()),
    path('books/create/', views.CreateBook.as_view()),
    path('books/<int:book_id>/', views.RetrieveBookAPIView.as_view()),

    path('authors/', views.RetrieveAuthors.as_view()),
    path('authors/create/', views.CreateAuthor.as_view()),
    path('authors/<int:author_id>/', views.RetrieveAuthorAPIView.as_view()),

    path('authors/', AuthorViewSet.as_view({'get':'list'})),
    path('authors/create/', AuthorViewSet.as_view({'post':'create'})),
    path('authors/<int:author_id>/', AuthorViewSet.as_view(
        {
            'get':'retrieve', 
            'put':'partial_update',
            'delete':'destroy'
        }
    )),
]