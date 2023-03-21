from django.urls import path
from .views import newsView, detail_View

urlpatterns = [
    path('', newsView, name='allNews'),
    path('<int:pk>/', detail_View.as_view(), name='detail_news'),
]