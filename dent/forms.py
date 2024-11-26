from captcha.widgets import ReCaptchaV2Invisible
from django import forms
from captcha.fields import ReCaptchaField



class ContactForm(forms.Form):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control w-100'}))
    surname = forms.CharField(min_length=2,
                          widget=forms.TextInput(attrs={'placeholder': 'Your surname', 'class': 'form-control w-100'}))

    phone = forms.CharField(min_length=2,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Your phone number', 'class': 'form-control w-100'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control w-100'}))


    message = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'placeholder': 'Message', 'cols': 30, 'rows': 9,
                                                                          'class': 'form-control w-100'}))
    captcha = ReCaptchaField(required=True)




class BaseContactForm(forms.Form):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control w-100'}))


    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control w-100'}))


    message = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'placeholder': 'Message', 'cols': 30, 'rows': 9,
                                                                          'class': 'form-control w-100'}))
    captcha = ReCaptchaField(required=True)







