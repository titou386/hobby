from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    CategoryListView,
    CategoryDetailView,
    TagListView,
    TagDetailView,
)

app_name = "blog"
urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("home/", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<slug:slug>/update/", ArticleUpdateView.as_view(), name="article_update"),
    path("<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/<slug:slug>/", TagDetailView.as_view(), name="tag_detail"),
]
