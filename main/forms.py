from django import forms
from .models import Recipie_Model, Image_Model


class Add_recipe(forms.ModelForm):
    class Meta:
        model = Recipie_Model
        fields = ('title', 'ingred', 'rec_body', 'yt_link', 'img',)
        labels = {
            'img': 'Картинка',
            'title': 'Название*',
            'ingred': 'Ингредиенты*',
            'rec_body': 'Рецепт*',
            'yt_link': 'Ссылка на видео',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'ingred': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ингредиенты и граммовки'}),
            'rec_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст рецепта'}),
            'yt_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка на видео youtube'}),
        }


class Add_Image(forms.ModelForm):
    class Meta:
        model = Image_Model
        fields = ('image',)
