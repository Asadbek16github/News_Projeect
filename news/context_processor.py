from .models import News, Category

def NewsProcessor(request):
    newsProcessor_news = News.objects.filter(status=News.Status.Published).order_by('-published_time')[:10]
    newsProcessor_categories = Category.objects.all()

    context = {
        'newsProcessor_news':newsProcessor_news,
        'newsProcessor_categories': newsProcessor_categories
    }

    return context