from users.models import CustomUser
from datetime import date


def get_birthday_user(request):
    birthday_users = CustomUser.objects.filter(birthday=date.today()).only(
        'email',
        'username')
    return {'birthday_users': birthday_users}
