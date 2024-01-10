from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import NewsLater, Post, Comment
from django.views import View
from django.views.generic import ListView


class AllPostBlog(ListView):
    model = Post
    template_name = 'blog/all_post_blog.html'
    paginate_by = 20
    context_object_name = 'all_post_blog'
    
    def get_queryset(self):
        return get_list_or_404(Post, is_active=True)


class BlogDetailsView(View):
    def get(self, request, *args, **kwargs):
        details = get_object_or_404(Post, slug=kwargs['slug'])
        return render(request, 'blog/blog_details.html', {'details': details})