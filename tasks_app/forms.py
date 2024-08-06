from django import forms

from tasks_app.models import WorkField


class FieldAddForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите название поля",
            }
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите описание поля",
            }
        ),
        required=False,
    )

    class Meta:
        model = WorkField
        fields = ["name", "description"]
