import functools
user = {
    'username': 'Pannu',
    'password': '1234Ad',
    'access_level': 'admin'
}


def check_user(func):
    @functools.wraps(func)
    def secure_func(panel):
        """Allows to retrive the password for admin panel """
        if user.get('access_level') == 'admin':
            return func(panel)
    return secure_func


@check_user
def func(panel):  # without arument
    """
    Allows us to make a checkuser decorator
    """
    return f"Admin {panel} password is 1234."


# @check_user
# def temp():
#     return 'Kem party maja ma.'


seecc = check_user('admin')(func)
print(func.__name__)
print(func.__doc__)
# print(temp())
