from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('books/<int:idBook>', views.showBook),
    path('bookAuthor/<int:idBook>',views.bookAuthor)
]