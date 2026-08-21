from .models import Category ,SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def social_links(request):
    return {'social_links': SocialLink.objects.all()}