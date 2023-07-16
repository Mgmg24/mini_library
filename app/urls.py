from django.urls import path 
from app import views

urlpatterns = [
    # path('all_book/',views.all_books,name='all_book'),
    path('category_books/<int:id>',views.category_books,name='category_books'),
    path('view_book/<int:id>',views.view_book,name='view_book'),
    path('',views.SearchView.as_view(),name='search_view'),
]
