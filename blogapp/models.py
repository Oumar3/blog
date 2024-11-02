from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from authentification.models import CustomUser

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    body = RichTextField()
    image = models.ImageField(upload_to="Articles_Img",null=True,blank=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now=True)

    def get_detail_article_url(self):
        return reverse("blogapp:detail-article", kwargs={"pk": self.pk})
    
    def get_image(self):
        if self.image:
            return self.image.url
        return None
    
    
    def __str__(self):
        return self.title