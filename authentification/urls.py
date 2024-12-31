from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth import views as auth_views

app_name = "auth"
urlpatterns = [
    path('login/',loginform,name='loginin'),
    path('logout/',logout_view,name='logout'),
    path('registerform/',registerform,name='registerform'),

    # URL pour afficher le formulaire de réinitialisation
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        extra_email_context={'protocol': 'http', 'domain': '127.0.0.1:8000'},
        email_template_name='password_reset_email.html',
        success_url=reverse_lazy('auth:password_reset_done')
        ), name='password_reset'),
    # URL après la soumission du formulaire de réinitialisation
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    # URL pour confirmer la réinitialisation du mot de passe
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    # URL après la confirmation du mot de passe
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
