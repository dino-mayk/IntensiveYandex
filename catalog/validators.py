from functools import wraps

from django.core.exceptions import ValidationError


def validate_must_be_param(*parameters):
    @wraps(validate_must_be_param)
    def validate(value):
        if parameters[0] not in value.lower() \
                and parameters[1] not in value.lower():
            raise ValidationError(
                f'обязательно используйте слова {parameters[0], parameters[1]}'
            )
        return value
    return validate
