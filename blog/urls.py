from django.urls import path, re_path
from .views import AllPostBlog, BlogDetailsView, CategoryBlogView, LatestBlogPostView


app_name = 'blog'
urlpatterns = [
    path('blog/', AllPostBlog.as_view(), name='all_posts'),
    path('blog_details/<slug:slug>/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    path('all_category/', CategoryBlogView.as_view(), name='category'),
    path('latest_post/', LatestBlogPostView.as_view(), name='latest_post'),
]
