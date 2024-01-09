from django.urls import path
from .views import AllPostBlog


app_name = 'blog'
urlpatterns = [
    path('blog/', AllPostBlog.as_view(), name='all_posts'),
]
