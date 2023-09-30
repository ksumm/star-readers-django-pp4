from django import forms
from django.forms import ModelForm
from .models import Post, Comment, Contact

class AddPost(forms.ModelForm):

    class Meta:
        model = Post
        fields =  (
            'title',
            'author',
            'content',
            'featured_image',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                        'label': 'name'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),                              
        }


        labels = {
            'title': 'Book Title',
            'content': 'Your review',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    """
    Contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'        