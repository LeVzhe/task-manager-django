from django import forms

from tasks_app.models import WorkField, Task


class TaskAddForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите название поля",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["content"]


class FieldAddForm(forms.ModelForm):
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
