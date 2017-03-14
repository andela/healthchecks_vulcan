from django import forms
from hc.blog.models import Post
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {
            'text': _(''),
            'title': _('')
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class':'form-control', 'placeholder':'Insert your blogpost here'}),
            'title': forms.Textarea(attrs={'cols': 75, 'rows': 1, 'class':'form-control', 'placeholder':'Insert post title here'}),

        }
