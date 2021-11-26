from django.urls import path
from .views import ArticleView,ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('article/<int:pk>/', ArticleUpdateView.as_view()),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view()),
]