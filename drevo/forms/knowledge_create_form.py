from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import inlineformset_factory
from mptt.forms import TreeNodeChoiceField

from drevo.models import Znanie, Category, ZnImage, Label
from drevo.models.utils import get_model_or_stub


class ZnanieCreateForm(forms.ModelForm):
    """
    Форма создания сущности Знание
    """
    name = forms.CharField(widget=forms.Textarea(attrs={'cols': 40,
                                                        'rows': 3,
                                                        }
                                                 ),
                           label='Тема'
                           )
    content = forms.CharField(widget=CKEditorWidget(attrs={'cols': 40,
                                                           'rows': 10,
                                                           }
                                                    ),
                              label='Содержание',
                              required=False
                              )

    category = TreeNodeChoiceField(queryset=get_model_or_stub(Category).tree_objects.all(),
                                   empty_label="(нет категории)",
                                   label='Категория',
                                   required=False)
    labels = forms.ModelMultipleChoiceField(queryset=Label.objects.all(), label='Метки', required=False)

    class Meta:
        model = Znanie
        exclude = ('id', 'date', 'updated_at', 'user', 'expert', 'redactor', 'director', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_send':
                field.widget.attrs['class'] = 'form-control'


ZnImageFormSet = inlineformset_factory(
    Znanie,
    ZnImage,
    fields=('photo',),
    extra=3,
    can_delete=False
)
