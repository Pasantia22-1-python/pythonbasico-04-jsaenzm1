PASSWORD = '12345'

def password_requiered(func):
    def wrapper(): 
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD: 
            return func()
        else: 
            print('Lac cotraseña no es correcta')

    return wrapper


@password_requiered
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@upper
def say_my_name(name):
    return 'hola {}'.format(name)


if __name__ == '__main__':
    'needs_password()'
    print(say_my_name('Rocio'))