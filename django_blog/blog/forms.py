from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'pic','author', 'content')
        widgets = {
            
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add title here',
                }),
            'title_tag': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add title tag here',
                }),
            'author': forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Add author name here',
                }),
            'content': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Add content of the blog here',
                }),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','pic','content')
        labels={
            'title':'Title',
            'title_tag': 'Title tag',
            'pic': 'Change Pic',
            'content': 'Content',
            
        }
        widgets = {
            
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add title here',
                }),
            'title_tag': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add title tag here',
                }),
            'content': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Add content of the blog here',
                }),
        }