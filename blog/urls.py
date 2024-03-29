from django.urls import path
from .views import AllPostBlog, BlogDetailsView, LatestBlogPostView


app_name = 'blog'
urlpatterns = [
    path('blog/', AllPostBlog.as_view(), name='all_posts'),
    path('blog_details/<slug:slug>/<int:pk>/', BlogDetailsView.as_view(), name='blog_details'),
    # path('all_category/', CategoryBlogView.as_view(), name='category'),
    path('latest_post/', LatestBlogPostView.as_view(), name='latest_post'),
    path('slug/<slug:category_slug>/', AllPostBlog.as_view(), name='post_by_category')
]
