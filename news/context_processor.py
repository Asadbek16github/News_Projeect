from .models import News

def NewsProcessor(request):
    all_news = News.objects.all()

    context = {
        'all_news':all_news
    }

    return context