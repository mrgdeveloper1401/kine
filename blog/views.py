from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
    form_class = Commentform
    template_name = 'blog/blog_details.html'
    
    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.post_instance = get_object_or_404(Post, pk=kwargs['pk'], slug=kwargs['slug'], is_active=True)
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        post = self.post_instance
        main_comment = Comment.objects.filter(status=True, posts_id=post.id, parent=None)
        return render(request, self.template_name, {'details': post, 'comment': main_comment, 'form': form})

    method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.posts = self.post_instance
            new_comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد بعد از تایید ان به نمایش در خواهد آمد', 'success')
            return redirect('blog:blog_details', pk=kwargs['pk'], slug=kwargs['slug'])
        return render(request, self.template_name, {'form': form})


class CategoryBlogView(View):
    def get(self, request, *args, **kwargs):
        main_category = CategoryBlog.objects.filter(parent=None)
        return render(request, 'blog/category_blog.html', {'category': main_category})


class LatestBlogPostView(View):
    def get(self, request, *args, **kwargs):
        latest_post = Post.objects.filter(is_active=True)[:10]
        return render(request, 'blog/latest_post.html', {'latest_post': latest_post})
