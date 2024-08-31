from django.contrib.auth.models import User
from django import forms


class MyUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("firs_name")
        last_name = cleaned_data.get("last_name")
        if not first_name and not last_name:
            raise forms.ValidationError('Please fill out either the First Name or Last Name field!')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
