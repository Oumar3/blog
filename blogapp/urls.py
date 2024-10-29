from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail-article/<int:pk>',views.detail_article_view,name='detail-article')
]
