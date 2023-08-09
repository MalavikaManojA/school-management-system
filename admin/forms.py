from django import forms
from .models import StaffDetail,Subject
from accounts.models import User

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password=forms.CharField(
        widget=forms.PasswordInput())
    confirm_password=forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput())

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['first_name','last_name','username','email','phone','date_of_birth','photo','password',]

class StaffDetailForm(forms.ModelForm):
    """Form definition for StaffDetail."""

    class Meta:
        """Meta definition for StaffDetailform."""

        model = StaffDetail
        exclude=('staff_name',)


class UserEditForm(forms.ModelForm):
    """Form definition for UserEdit."""

    class Meta:
        """Meta definition for UserEditform."""

        model = User
        fields = ['first_name','last_name','username','email','phone','date_of_birth','photo',]

class SubjectForm(forms.ModelForm):
    """Form definition for Subjects."""

    class Meta:
        """Meta definition for Subjectsform."""

        model = Subject
        fields = '__all__'


