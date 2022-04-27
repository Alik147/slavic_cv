from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        exclude = {'id'}
        labels = {
            'storage': 'Хранилище',
            'fond': 'Фонд',
            'inventory': 'Опись',
            'number': '№ рукописи',
            'exodus': 'Извод',
            'months': 'Месяцы',
            'months_numbers': '№ месяцев',
            'dating': 'Датировка',
            'size': 'Листов',
            'book_format': 'Формат',
            'book_type': 'Тип',
            'file_path': 'Файлы',
            'handwriting': 'Почерк',
            'material': 'Материал',
            'description': 'Описание',
            'additional_info': 'Примечание'
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'university-form'
        self.helper.add_input(Submit('сохранить', 'Сохранить'))