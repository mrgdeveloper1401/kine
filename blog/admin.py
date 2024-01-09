from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'create_at')
    list_editable = ('is_active', )
    list_filter = ('is_active', 'create_at', 'update_at')
    date_hierarchy = 'create_at'
    list_per_page = 20
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('user',)
    search_fields = ('title',)