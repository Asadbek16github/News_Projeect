from django.urls import path
from .views import (    newsView, detail_View, contactPageView, 
                        page_404_view, HomePageView, LocalPageView,
                        NewsDelete, NewsUpadete, NewsCreatePageView
                    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact/', contactPageView, name='contact_page'),
    path('404/', page_404_view, name='404'), 
    path('news/', newsView, name='allNews'),
    path('news/<slug:news>/', detail_View, name='detail_news'),
    path('news/delete/<slug>/', NewsDelete.as_view(), name='delete_news'),
    path('news/update/<slug>/', NewsUpadete.as_view(), name='update_news'),
    path('news/create', NewsCreatePageView.as_view(), name='create_page'),
    path('local/', LocalPageView.as_view(), name='local_news_page'),
]