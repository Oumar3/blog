from django.urls import path
from . import views
app_name = "auth"
urlpatterns = [
    path('login/',views.loginform,name='loginin'),
    path('logout/',views.logout_view,name='logout'),
    path('registerform/',views.registerform,name='registerform'),
]
