from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import dashboard

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('dashboard/', dashboard, name='dashboard_page')
]