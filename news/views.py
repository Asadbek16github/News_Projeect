from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category
from django.views.generic import DetailView
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

def homePageView(request):
    all_news = News.objects.filter(status=News.Status.Published)
    all_categories = Category.objects.all()

    context = {
        'all_news':all_news,
        'all_categories':all_categories,
    }

    return render(request, 'news/index.html', context=context)


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
