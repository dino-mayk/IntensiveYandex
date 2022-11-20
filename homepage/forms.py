from django.db import models


class LoginModel(models.Model):
    name = models.CharField(
        'Имя',
        
    )
    email = models.EmailField(

    )


class Form(models.ModelForm):
    class Meta:
        model = Model
        fields = (

        )
        labels = {
            'name': 'Имя'
        }
        help_texts = {
            'name': 'Моя помогать'
        }

