from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'pic','author','content','snippet')
        widgets = {
            
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Add title here',
                }),
            'title_tag': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'add title tag here',
                }),
            'author': forms.TextInput(attrs={
                'class':'form-control',
                'value':'',
                'id':'elder',
                'type': 'hidden'
                }),
            'content': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Add content of the blog here',
                }),
            'snippet': forms.Textarea(attrs={
                'class':'form-control',
               
                }),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','pic','content','snippet')
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
            'snippet': forms.Textarea(attrs={
                'class':'form-control',
                }),
        }