from django.urls import path
from .views import dashboard, signUp
from django.contrib.auth.views import ( LoginView, LogoutView, PasswordChangeView,
                                        PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,
                                        PasswordResetCompleteView, PasswordResetConfirmView
                                        )

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('dashboard/', dashboard, name='dashboard_page'),
    path('passwordChange/', PasswordChangeView.as_view(), name='password_change_page'),
    path('passwordChangeDone/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('signUp/', signUp, name='signUp'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-rest/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-rest/complate/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]