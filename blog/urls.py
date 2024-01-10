from django.urls import path, re_path
from .views import AllPostBlog, BlogDetailsView, CategoryBlogView


app_name = 'blog'
urlpatterns = [
    path('blog/', AllPostBlog.as_view(), name='all_posts'),
    path('blog_details/<str:slug>/', BlogDetailsView.as_view(), name='blog_details'),
    path('all_category/', CategoryBlogView.as_view(), name='category'),
]
