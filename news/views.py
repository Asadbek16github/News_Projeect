from django.shortcuts import render
from .models import News, Category
from django.views.generic import DetailView

# Create your views here.
def newsView(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news
    }

    return render(request, 'news/allNews.html', context=context)

class detail_View(DetailView):
    model = News
    template_name = 'news/detail.html'

def homePageView(request):
    all_news = News.objects.filter(status=News.Status.Published)
    all_categories = Category.objects.all()

    context = {
        'all_news':all_news,
        'all_categories':all_categories,
    }

    return render(request, 'news/index.html', context=context)
