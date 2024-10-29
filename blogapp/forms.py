from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100,null=True,blank=True)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(upload_to="Articles_Img",null=True,blank=True)

    def clean_field(self):
        data = self.cleaned_data["field"]
        
        return data
    
