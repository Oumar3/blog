from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,CustomUser
from authentification.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.views.generic import ListView,DetailView,TemplateView,View



class blogListView(View):
    # model = Article
    # queryset = Article.objects.select_related('author').all()
    template_name = 'pages/index.html'
    # context_object_name = 'articles'
    # paginate_by = 10

    def get(self, request, *args, **kwargs):
        queryset = Article.objects.select_related('author').all()
        # Récupérer l'utilisateur
        # content_type = ContentType.objects.get(app_label='blogapp', model='article')
        # permission_exists = Permission.objects.filter(content_type=content_type, codename='can_add_ali').exists()
        
        # if permission_exists:
        #     print("La permission 'can_add_item' existe.")
        # else:
        #     print("La permission 'can_add_item' n'existe pas.")
        
        context = {
            'articles':queryset
        }
        return render(request,self.template_name,context)
class detail_article_views(DetailView):
    model = Article
    template_name = 'pages/detail_article.html'
    context_object_name = 'article'

# Create your views here.
def home(request,*args,**kwargs):
    articles = Article.objects.select_related('author').all()
    # Récupérer l'utilisateur
    content_type = ContentType.objects.get(app_label='blogapp', model='article')

# Vérifier si la permission existe
    permission_exists = Permission.objects.filter(content_type=content_type, codename='can_add_ali').exists()
    
    if permission_exists:
        print("La permission 'can_add_item' existe.")
    else:
        print("La permission 'can_add_item' n'existe pas.")

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