from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from app.models import GroupAccess, UserGroup, Organization, OrganizationsClientChargeCode, OrganizationsCarrierDetail


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

    def __init__(self, *args, **kwargs):
        cat_name = kwargs.pop('cat_name', None)
        super(OrganizationForm, self).__init__(*args, **kwargs)
        if cat_name == dict(Organization.CATEGORIES_CHOICES).get(Organization.CLIENT).lower():
            self.fields['category'].initial = Organization.CLIENT
        if cat_name == dict(Organization.CATEGORIES_CHOICES).get(Organization.CUSTOMER).lower():
            self.fields['category'].initial = Organization.CUSTOMER
        if cat_name == dict(Organization.CATEGORIES_CHOICES).get(Organization.CARRIER).lower():
            self.fields['category'].initial = Organization.CARRIER

        if self.instance and self.instance.pk or cat_name:
            self.fields['category'].widget = forms.HiddenInput()


class OrganizationsClientChargeCodeForm(forms.ModelForm):
    class Meta:
        model = OrganizationsClientChargeCode
        fields = '__all__'


class OrganizationsCarrierDetailForm(forms.ModelForm):
    class Meta:
        model = OrganizationsCarrierDetail
        fields = '__all__'
