from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import NewsLater, Post, Comment
from django.views import View
from django.views.generic import ListView


class AllPostBlog(ListView):
    model = Post
    queryset = get_list_or_404(Post, is_active=True)
    template_name = 'blog/all_post_blog.html'
    paginate_by = 20
    context_object_name = 'all_post_blog'