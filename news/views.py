from django.shortcuts import render
from .models import News
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

