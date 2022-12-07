from users.models import CustomUser
from datetime import date


def get_birthday_user(request):
    birthday_user = CustomUser.objects.filter(birthday=date.today())
    return {'birthday_user': birthday_user}
