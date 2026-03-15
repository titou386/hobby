from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article, Category, Tag

class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(published=True).order_by("-created_at")

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_queryset(self):
        return Article.objects.filter(published=True)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["title", "content", "categories", "tags", "featured_image"]
    success_url = reverse_lazy("blog:article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["title", "content", "categories", "tags", "featured_image"]
    success_url = reverse_lazy("blog:article_list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = self.get_object()
        return context

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:article_list")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

class CategoryListView(ListView):
    model = Category
    template_name = "blog/category_list.html"
    context_object_name = "categories"

class TagListView(ListView):
    model = Tag
    template_name = "blog/tag_list.html"
    context_object_name = "tags"

class CategoryDetailView(ListView):
    model = Article
    template_name = "blog/category_detail.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs["slug"])
        return Article.objects.filter(categories=category, published=True).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs["slug"])
        return context
