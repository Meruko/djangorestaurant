from .models import Dish, Ingridient
from django.forms import ModelForm, TextInput, NumberInput

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'default_price']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'default_price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Базовая стоимость'
            })
        }

class IngridientForm(ModelForm):
    class Meta:
        model = Ingridient
        fields = ['name', 'price', 'count']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во'
            })
        }