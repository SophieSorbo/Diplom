from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, FileInput
from django import forms



class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Подпись'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Фото'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
        }