from django.http import HttpResponse
from django.shortcuts import render
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

class detail_View(DetailView):
    model = News
    template_name = 'news/detail.html'


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
        context['news'] = News.objects.filter(status=News.Status.Published).order_by('-published_time')[:4]
        context['last_local_news_one'] = News.objects.filter(status=News.Status.Published).filter(category__category='Mahalliy')[:1]
        context['last_local_news'] = News.objects.filter(status=News.Status.Published).filter(category__category='Mahalliy')[1:5]

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
