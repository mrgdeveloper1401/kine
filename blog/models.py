from django.db import models
from common.models import CreateAt, UpdateAt
from django.utils.translation import gettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class NewsLater(CreateAt):
    email = models.EmailField(_('Email'), max_length=254)
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = 'doctor_news_later'
        verbose_name = _('News Later')
        verbose_name_plural = _('News Later')


class CategoryBlog(MPTTModel,CreateAt, UpdateAt):
    title = models.CharField(_('Title'), max_length=100)
    is_active = models.BooleanField(_("فعال"), default=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'category_blog'
        verbose_name = _('category blog')
        verbose_name_plural = _('category blog')

class Post(CreateAt, UpdateAt):
    category = models.ManyToManyField(CategoryBlog, related_name='category_post')
    title = models.CharField(_('Title'), max_length=254, unique=True)
    short_description = models.CharField(_('short description'), blank=True, null=True, max_length=100)
    slug = models.SlugField(max_length=254, unique=True, allow_unicode=True)
    image = models.ImageField(_('Image'), upload_to='blog/%Y/%M/%d', width_field='', height_field='')
    width_image = models.PositiveIntegerField(blank=True, null=True)
    height_image = models.PositiveIntegerField(blank=True, null=True)
    body = models.TextField()
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='posts')
    is_active = models.BooleanField(default=False)
   
    
    def __str__(self) -> str:
        return f'{self.title} -- {self.short_description}'
    
    class Meta:
        ordering = ('-create_at',)
        verbose_name = _('posts')
        verbose_name_plural = _('posts')


class Comment(CreateAt):
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_comments')
    posts = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post_comments')
    body = models.TextField()

    def __str__(self) -> str:
        return self.body

    class Meta:
        db_table = 'comment'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
