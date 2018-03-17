from django import forms
from AppTwo.models import User


class NewUserForm(forms.ModelForm):

    # might want to add in custom validation here

    class Meta():
        model = User  # if more models, multiple Meta
        fields = '__all__'
