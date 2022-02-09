from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("პაროლი"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),

    )
    password2 = forms.CharField(
        label=_("გაიმეორე პაროლი"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-1 px-2 mb-2 leading-tight focus:outline-none focus:bg-white'

        for field in self.fields.values():
            field.error_messages = {
                'required': '{fieldname} შევსება სავალდებულოა '.format(
                fieldname=field.label),
                'unique':'ასეთი {fieldname} უკვე არსებობს'.format(
                fieldname=field.label)}

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "password1",
            "password2",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("პაროლები არ ემთხვევა")
        if len(password1) < 8:
            raise ValidationError('პაროლი უნდა იყოს მინიმუმ 8 სიმბოლოსგან')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label=_("პაროლი"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    error_messages = {
        'invalid_login': _(
            "პაროლი ან მაილი არასწორია"
        ),
    }
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

        for field in self.fields.values():
            field.error_messages = {
                    'required': 'შევსება სავალდებულოა'}