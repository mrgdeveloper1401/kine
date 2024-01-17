from django.contrib import admin
from .models import Post, CategoryBlog, NewsLater, Comment
from django_jalali.admin.filters import JDateFieldListFilter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('category',
         {'fields': ('category', 'user')}),
        ('add posts',
         {'fields': ('title', 'en_title', 'slug', 'body', 'image', 'is_active', 'create_at', 'update_at')})
    ]
    list_display = ('title', 'en_title', 'show_category', 'user', 'is_active', 'create_at', 'id')
    list_editable = ('is_active', )
    list_filter = (
        ('create_at', JDateFieldListFilter),
        ('update_at', JDateFieldListFilter),
        'is_active'
    )
    date_hierarchy = 'create_at'
    list_per_page = 20
    prepopulated_fields = {'slug': ('en_title', )}
    raw_id_fields = ('user',)
    search_fields = ('title',)
    filter_horizontal = ('category',)
    readonly_fields = ('create_at', 'update_at')
    
    def show_category(self, obj):
        return ','.join([c.title for c in obj.category.all()])


@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_active', 'slug', 'id')
    list_filter = (
        ('create_at', JDateFieldListFilter),
        ('update_at', JDateFieldListFilter),
        'is_active'
    )
    list_editable = ('is_active',)
    date_hierarchy = 'create_at'
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'posts', 'status', 'body', 'parent', 'id')
    list_filter = (('create_at', JDateFieldListFilter), 'status')
    list_per_page = 30
    search_fields = ('body',)
    date_hierarchy = 'create_at'
    raw_id_fields = ('user', 'posts')
    list_editable = ('status',)
