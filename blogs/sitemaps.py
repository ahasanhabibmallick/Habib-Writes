from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Blog.objects.filter(status='Published')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        from django.urls import reverse
        return reverse('blogs', args=[obj.slug])
