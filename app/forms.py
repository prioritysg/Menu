from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app.models import GroupAccess


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254, label='UserName',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Username already exist")
        return username


class GroupAccessForm(forms.ModelForm):
    class Meta:
        model = GroupAccess
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupAccessForm, self).__init__(*args, **kwargs)
        self.fields['user_group'].widget.attrs['disabled'] = 'disabled'
