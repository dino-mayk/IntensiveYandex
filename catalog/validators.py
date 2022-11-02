from django.core.exceptions import ValidationError
from functools import wraps


def validate_must_be_param(*parameters):
    @wraps(validate_must_be_param)
    def validate(value):
        if (parameters[0] not in value.lower()) \
                and (parameters[1] not in value.lower()):
            raise ValidationError(
                f'Обязательно используйте слова {parameters[0], parameters[1]}'
            )
        return value
    return validate
