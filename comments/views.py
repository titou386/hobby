from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment
from blog.models import Article

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    template_name = "comments/add_comment.html"

    def form_valid(self, form):
        article = Article.objects.get(slug=self.kwargs["slug"])
        form.instance.article = article
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={"slug": self.kwargs["slug"]})

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments/delete_comment.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={"slug": self.kwargs["article_slug"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_slug"] = self.kwargs["article_slug"]
        return context
