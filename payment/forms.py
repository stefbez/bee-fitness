from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'phone_number',
                  'first_line_address', 'postcode')


# class UserInfoForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     phone_number = forms.CharField(max_length=100)
#     first_line_address = forms.CharField(max_length=100)
#     postcode = forms.CharField(max_length=100)
