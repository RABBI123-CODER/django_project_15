import email
from django import forms


class teacher_registration(forms.Form):
    first_name = forms.CharField(label='Enter your first name', label_suffix=' ')
    last_name = forms.CharField(initial='study mart')
    email = forms.EmailField(initial='rabiulhasanrabbi123@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget = forms.Textarea)
    file = forms.CharField(widget = forms.FileInput)
    checkbox = forms.CharField(widget = forms.CheckboxInput)
