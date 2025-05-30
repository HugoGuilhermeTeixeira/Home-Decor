from django.shortcuts import render
from products.models import Product
from blog.models import Article

def index(request):
    featured_products = Product.objects.filter(is_featured=True).order_by('-created_at')[:3]
    latest_articles = Article.objects.filter(is_published=True).order_by('-created_at')[:3]
    
    context = {
        'featured_products': featured_products,
        'latest_articles': latest_articles,
    }
    return render(request, 'core/index.html', context)
