from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ваше ИМЯ'}),error_messages={'required': 'Введите Ваше имя'})
    email =  forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ваше Email для связи'}),error_messages={'required': 'Введите Ваш Email'})
    #number_phone = forms.CharField(max_length=50)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control text', 'placeholder':'Ваше сообщение'}),error_messages={'required': 'Введите сообщение'})
    captcha = CaptchaField(label='Введите код с картинки:', error_messages={'required': 'Неверный код'})
    
