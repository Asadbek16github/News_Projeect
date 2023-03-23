from django.urls import path
from .views import newsView, detail_View, homePageView, contactPageView

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('contact/', contactPageView, name='contact_page'),
    path('news/', newsView, name='allNews'),
    path('news/<int:pk>/', detail_View.as_view(), name='detail_news'),
]