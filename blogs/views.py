from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect,HttpResponse
from .models import Blog,Category, SocialLink, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.select_related('category').filter(status='Published', category=category_id).order_by('-created_at')
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category_id' : category,
    }

    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug, status='Published')

    # Increment view count safely (ignore errors on read-only filesystems like Vercel)
    try:
        single_blog.view_count += 1
        single_blog.save()
    except Exception:
        pass

    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        try:
            comment.save()
            return HttpResponseRedirect(request.path_info)
        except Exception:
            # Handle read-only error gracefully
            return HttpResponse("Commenting is currently disabled on this demo version.")

    # Comments
    comments = Comment.objects.filter(blog=single_blog).order_by('-created_at')

    # Related Articles
    related_articles = Blog.objects.filter(category=single_blog.category, status='Published').exclude(id=single_blog.id)[:3]

    context ={
        'single_blog': single_blog,
        'comments': comments,
        'related_articles': related_articles,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')

    blogs =Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    print(blogs)

    context ={
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request,'search.html',context)