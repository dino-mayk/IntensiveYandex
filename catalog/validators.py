from django.core.exceptions import ValidationError


def validate_amazing(value):
    must_be_in_your_item = ['превосходно', 'роскошно']

    if (must_be_in_your_item[0] not in value.lower()) and \
            (must_be_in_your_item[1] not in value.lower()):
        raise ValidationError(
            f'Обязательно используйте слова {", ".join(must_be_in_your_item)}'
        )

    return value
