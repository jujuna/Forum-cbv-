from django import forms
from .models import Comment, Question
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from  User.models import User


class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-20 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white'})
        self.fields['text'].widget.attrs['placeholder'] = 'დაამატე კომენტარი'
        self.fields['text'].required=True
        self.fields['text'].error_messages = {'required': 'შევსება აუცილებელია!'}


    class Meta:
        model = Comment
        fields = ["text"]


class QuestionForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-12 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        self.fields['title'].widget.attrs['placeholder'] = 'სათაური'
        self.fields['title'].error_messages = {'required': 'სათაური აუცილებელია!'}
        self.fields['text'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-20 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        self.fields['text'].error_messages = {'required': 'დასვი კითხვა'}
        self.fields['text'].widget.attrs['placeholder'] = 'კითხვა'
        self.fields['category'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-20 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        self.fields['category'].error_messages = {'required': 'აირჩიე კატეგორია'}



    class Meta:
        model = Question
        fields = ["title", "text", "category"]


class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['username'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-12 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        self.fields['email'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-12 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        self.fields['mobile'].widget.attrs.update({'class': 'bg-gray-100 rounded border border-gray-400 leading-normal resize-none w-full h-12 py-2 px-3 font-medium placeholder-gray-700 focus:outline-none focus:bg-white mb-4 text-center'})
        print(instance.update_access())
        if not instance.update_access():
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['mobile'].disabled = True

    class Meta:
        model = User
        fields = ["username", "email", "mobile"]
