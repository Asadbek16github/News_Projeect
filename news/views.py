from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import News, Category
from django.views.generic import DetailView, ListView
from .forms import ContactForm

# Create your views here.
def newsView(request):
    all_news = News.objects.all()

    context = {
        'all_news': all_news
    }

    return render(request, 'news/allNews.html', context=context)

# class detail_View(DetailView):
#     model = News
#     template_name = 'news/detail.html'

def detail_View(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        'news':news
    }
    return render(request, 'news/detail.html', context=context)


# home page view funcksiya orqali yozilgan
# def homePageView(request):
#     all_news = News.objects.filter(status=News.Status.Published)[:5]
#     all_categories = Category.objects.all()
#     last_local_news_one = News.objects.filter(status=News.Status.Published).filter(category__category='Mahalliy')[:1]
#     last_local_news = News.objects.filter(status=News.Status.Published).filter(category__category='Mahalliy')[1:6]

#     context = {
#         'all_news':all_news,
#         'all_categories':all_categories,
#         'last_local_news_one':last_local_news_one,
#         'last_local_news':last_local_news
#     }

#     return render(request, 'news/index.html', context=context)

# Home page view class orqali yozilgan
class HomePageView(ListView):
    template_name = 'news/index.html'
    model = News
    context_object_name = 'all_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['news'] = News.objects.order_by('-published_time')[:4]
        context['mahalliy'] = News.objects.filter(category__category='Mahalliy')[:5]
        context['sport'] = News.objects.filter(category__category='Sport').order_by('-published_time')[:5]
        context['xorij'] = News.objects.filter(category__category='Xorij xabarlari').order_by('-published_time')[:5]
        context['lifestyle'] = News.objects.filter(category__category='lifestyle').order_by('-published_time')[:5]

        return context


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("Xabaringizga tez orada javob beramiz !")
    context = {
        'form':form
    }
    return render(request, 'news/contact.html', context)


def page_404_view(request):
    return render(request, 'news/404.html')

# Mahalliy page View
class LocalPageView(ListView):
    model = News
    template_name = 'news/mahalliyPage.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = News.objects.filter(status=News.Status.Published).filter(category__category='Mahalliy')

        return news