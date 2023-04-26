from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import dashboard, signUp

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('dashboard/', dashboard, name='dashboard_page'),
    path('passwordChange/', PasswordChangeView.as_view(), name='password_change_page'),
    path('passwordChangeDone/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('signUp/', signUp, name='signUp')
]