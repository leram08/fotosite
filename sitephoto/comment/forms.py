from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50,label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ваше ИМЯ'}), error_messages={'required': 'Введите Ваше имя'})
    email =  forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ваше Email'}),error_messages={'required': 'Введите Ваш email'})  
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control text', 'placeholder':'Ваш отзыв'}),error_messages={'required': 'Введите Ваш отзыв'})
    photo = forms.FileField(label='', error_messages={'required': 'Выберите фотографию'})
    captcha = CaptchaField(label='Введите код с картинки:', error_messages={'required': 'Неверный код'})
    
