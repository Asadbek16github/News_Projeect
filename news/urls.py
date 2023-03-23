from django.urls import path
from .views import newsView, detail_View, homePageView, contactPageView, page_404_view

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('contact/', contactPageView, name='contact_page'),
    path('404/', page_404_view, name='404'), 
    path('news/', newsView, name='allNews'),
    path('news/<int:pk>/', detail_View.as_view(), name='detail_news'),
]