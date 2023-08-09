import functools
user = {
    'username': 'Pannu',
    'password': '1234Ad',
    'access_level': 'admin'
}


def check_user(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        """Allows to retrive the password for admin panel """
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func


@check_user
def func(arg):  # without arument
    """
    Allows us to make a checkuser decorator
    """
    return "Admin panel password is 1234."


@check_user
def temp():
    return 'Kem party maja ma.'


print(func('admin'))

print(temp())
