from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'bg-gray-200 border-2 border-gray-200 rounded h-16 relative left-16 py-2 px-2  w-3/4 text-gray-700 focus:outline-none focus:bg-gray-300 focus:border-purple-500h-12 resize-none m-2'})

    class Meta:
        model = Comment
        fields = ["text"]