from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

STATUS_CHOICES =(
     ("Draft", "Draft"),
     ("Published", "Published")
)

class Blog(models.Model):
        title = models.CharField(max_length=200)
        slug = models.SlugField(max_length=150, unique=True, blank=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100)
        author = models.ForeignKey(User , on_delete=models.CASCADE)
        featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
        short_description = models.TextField(max_length=500)
        blog_body = models.TextField(max_length=2000)
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
        is_featured = models.BooleanField(default=False)
        tags = models.ManyToManyField(Tag, blank=True)
        view_count = models.PositiveIntegerField(default=0)
        seo_title = models.CharField(max_length=255, blank=True)
        seo_description = models.TextField(max_length=500, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
             return self.title
        
        @property
        def reading_time(self):
            # Average reading speed is 200 words per minute
            word_count = len(self.blog_body.split())
            minutes = word_count / 200
            return max(1, round(minutes))


class SocialLink(models.Model):
    platform = models.CharField(max_length=50) 
    link = models.URLField()

    def __str__(self):
        return self.platform    



class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
     comment = models.TextField(max_length=250)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)   


     def __str__(self):
          return self.comment