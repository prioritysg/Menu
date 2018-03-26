from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app.models import GroupAccess, UserGroup, Organization


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


class UserEditForm(forms.ModelForm):
    group = forms.ChoiceField(choices=UserGroup.USER_TYPES)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'group')


class UserAddForm(forms.ModelForm):
    group = forms.ChoiceField(choices=UserGroup.USER_TYPES)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'group', 'username')


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
        #     (
        # 'org_id', 'category', 'description', 'mt_address1', 'mt_address2', 'mt_address3', 'mt_city', 'mt_state',
        # 'mt_zip', 'mt_country', 'st_address1', 'st_address2', 'st_address3', 'st_city', 'st_state', 'st_zip',
        # 'st_country', 'active',)
