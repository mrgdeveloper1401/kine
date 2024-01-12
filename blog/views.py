from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import NewsLater, Post, Comment, CategoryBlog
from .form import Commentform


class AllPostBlog(ListView):
    model = Post
    template_name = 'blog/all_post_blog.html'
    paginate_by = 20
    context_object_name = 'all_post_blog'
    paginate_by = 20
    queryset = Post.objects.filter(is_active=True)


class BlogDetailsView(View):
    def get(self, request, *args, **kwargs):
        details = get_object_or_404(Post.active_post, slug=kwargs['slug'])
        return render(request, 'blog/blog_details.html', {'details': details})


class CategoryBlogView(View):
    def get(self, request, *args, **kwargs):
        main_category = CategoryBlog.objects.filter(parent=None)
        return render(request, 'blog/category_blog.html', {'category': main_category})


class LatestBlogPostView(View):
    def get(self, request, *args, **kwargs):
        latest_post = Post.objects.filter(is_active=True)[:10]
        return render(request, 'blog/latest_post.html', {'latest_post': latest_post})


class CommentPostView(View):
    form_class = Commentform
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'blog/comments.html', {'form': form})
    
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         Comment.objects.create(
    #             user = request.user,
    #             body = cd['body'],
    #             posts = 
    #         )
            