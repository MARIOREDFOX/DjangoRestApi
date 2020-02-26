from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleNewView, ArticleUpdate, ArticleDelete


urlpatterns = [
    path('articles',ArticleListView.as_view()),
    path('article/<int:pk>',ArticleDetailView.as_view()),
    path('article/new',ArticleNewView.as_view()),
    path('article/edit/<int:pk>',ArticleUpdate.as_view()),
    path('article/delete/<int:pk>',ArticleDelete.as_view()),
]
