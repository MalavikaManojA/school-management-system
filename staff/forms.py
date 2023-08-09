from django import forms
from .models import ParentDetail,Student_data
from student.models import MarkList

class Student_dataForm(forms.ModelForm):
    """Form definition for Student_data."""

    class Meta:
        """Meta definition for Student_dataform."""

        model = Student_data
        exclude=('student','parent','standard','teacher',)

class ParentDetailForm(forms.ModelForm):
    """Form definition for ParentDetail."""

    class Meta:
        """Meta definition for ParentDetailform."""

        model = ParentDetail
        fields = "__all__"

class MarkListForm(forms.ModelForm):
    """Form definition for MarkList."""

    class Meta:
        """Meta definition for MarkListform."""

        model = MarkList
        exclude = ['student','subject']

