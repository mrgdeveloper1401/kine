from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, Comment, CategoryBlog
from .form import Commentform, ReplyForm


class AllPostBlog(View):
    template_name = 'blog/all_post_blog.html'

    def get(self, request: HttpRequest, category_slug=None):
        posts = Post.objects.filter(is_active=True)
        category = CategoryBlog.objects.filter(is_active=True, parent=None)
        if category_slug:
            cat = CategoryBlog.objects.get(slug=category_slug)
            posts = posts.filter(category=cat)
        return render(request, self.template_name, {'all_post_blog': posts, 'category': category})


class BlogDetailsView(View):
    form_class = Commentform
    from_class_reply = ReplyForm
    template_name = 'blog/blog_details.html'

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.post_instance = get_object_or_404(Post, pk=kwargs['pk'], slug=kwargs['slug'], is_active=True)
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        post = self.post_instance
        main_comment = Comment.objects.filter(status=True, posts_id=post.id, parent=None)
        return render(request, self.template_name, {'details': post, 'comment': main_comment, 'form': form,
                                                    'reply_form': self.from_class_reply})

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


class LatestBlogPostView(ListView):
    model = Post
    template_name = 'blog/latest_post.html'
    queryset = model.objects.filter(is_active=True)[:10]
