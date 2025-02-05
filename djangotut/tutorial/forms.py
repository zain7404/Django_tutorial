from django import forms
from .models import courseType

class courseTypeForm(forms.Form):
    course_type = forms.ModelChoiceField(queryset=courseType.objects.all(),label='Select Course Type')