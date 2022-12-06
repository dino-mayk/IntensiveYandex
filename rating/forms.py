from django.forms import ModelForm

from rating.models import Mark


class AddMarkForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mark

        fields = (Mark.mark.field.name, )
        label = {
            Mark.mark.field.name: 'Оценка'
        }
