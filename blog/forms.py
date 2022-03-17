from django import forms

class PostForm(forms.Form):
    author = forms.CharField(label="author", max_length=50)
    title = forms.CharField(label="title", max_length=50)
    content = forms.CharField(label="content")


