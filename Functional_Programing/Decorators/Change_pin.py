def user(func):
    def wrapper(a,b):
        if a=='admin':
            return func(a,b)
        else:
            raise Exception('Not Allowed')
    return wrapper
@user
def change_pin(username,pin):
    # mypin=pin
    return pin
print(change_pin('admin',6336))