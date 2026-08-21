from django.contrib import admin
from  .models import Category, Blog, SocialLink, Comment, Tag
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'author', 'status', 'is_featured', 'view_count']
    search_fields = ('id', 'title', 'category__category_name', 'status', 'blog_body')
    list_editable = ('is_featured', 'status')
    list_filter = ('category', 'status', 'is_featured')
    filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'author', 'featured_image', 'status', 'is_featured')
        }),
        ('Content', {
            'fields': ('short_description', 'blog_body', 'tags')
        }),
        ('SEO & Metrics', {
            'fields': ('seo_title', 'seo_description', 'view_count'),
            'classes': ('collapse',),
        }),
    )

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)