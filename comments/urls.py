from django.urls import path
from .views import AddCommentView, DeleteCommentView

app_name = "comments"
urlpatterns = [
    path("add/<slug:slug>/", AddCommentView.as_view(), name="add_comment"),
    path("delete/<slug:article_slug>/<int:pk>/", DeleteCommentView.as_view(), name="delete_comment"),
]
