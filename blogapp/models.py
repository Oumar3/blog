from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    body = RichTextField()
    image = models.ImageField(upload_to="Articles_Img",null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now=True)

    def get_detail_article_url(self):
        return reverse("blogapp:detail-article", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title