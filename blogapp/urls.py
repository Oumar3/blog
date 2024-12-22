from django.urls import path
from . import views
app_name = 'blogapp'
urlpatterns = [
    path('',views.blogListView.as_view(),name='home'),
    path('detail-article/<int:pk>',views.detail_article_views.as_view(),name='detail-article')
]
