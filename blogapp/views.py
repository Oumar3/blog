from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
# Create your views here.
def home(request,*args,**kwargs):
    articles = Article.objects.select_related('author').all()
    context = {
        'articles':articles
    }
    return render(request,'pages/index.html',context)

def detail_article_view(request,pk,*args,**kwargs):
    article = get_object_or_404(Article.objects.select_related('author'),pk=pk)
    if article:
        context = {
            'article':article
        }
    return render(request,'pages/detail_article.html',context)