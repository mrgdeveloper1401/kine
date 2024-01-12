from django.contrib import admin
from .models import Post, CategoryBlog, NewsLater, Comment
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('category',
         {'fields': ('category', 'user')}),
        ('add posts',
         {'fields': ('title', 'slug', 'short_description', 'body', 'image', 'is_active', 'create_at', 'update_at')})
    ]
    list_display = ('title', 'user', 'is_active', 'create_at')
    list_editable = ('is_active', )
    list_filter = ('is_active', 'create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 20
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('user',)
    search_fields = ('title',)
    filter_horizontal = ('category',)
    readonly_fields = ('create_at', 'update_at')


@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_active',)
    list_filter = (
        ('create_at', JDateFieldListFilter),
        ('update_at', JDateFieldListFilter),
        'is_active'
    )
    list_editable = ('is_active',)
    date_hierarchy = 'create_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'status', 'body')
    list_filter = ('create_at', 'status')
    list_per_page = 30
    search_fields = ('body',)
    list_editable = ('body',)
    date_hierarchy = 'create_at'
    raw_id_fields = ('user', 'posts')
    