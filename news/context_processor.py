from .models import News

def NewsProcessor(request):
    newsProcessor_news = News.objects.filter(status=News.Status.Published).order_by('-published_time')[:10]

    context = {
        'newsProcessor_news':newsProcessor_news
    }

    return context