import functools
user = {
    'username': 'Pannu',
    'password': '1234Ad',
    'access_level': 'admin'
}


def anotherDec(access_level):
    def check_user(func):
        @functools.wraps(func)
        def secure_func(panel):
            """Allows to retrive the password for admin panel """
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return check_user


@anotherDec('admin')
def func(panel):  # without arument
    """
    Allows us to make a checkuser decorator
    """
    return f"Admin {panel} password is 1234."


# @check_user
# def temp():
#     return 'Kem party maja ma.'

secure = anotherDec('admin')(func)('admin')
print(secure)
# print(temp())

print(func("admin"))
