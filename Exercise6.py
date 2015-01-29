"""class MyError(StandardError):
    def __init__(self, arg):
        self.arg = arg
try:
    raise MyError("This is a user-defined error")
except MyError as me:
    print me.arg"""


def division(x, y):
        if y == 0:
            raise ZeroDivisionError

        return x / y


try:
    print division(8, 0)
except ZeroDivisionError:
    print "I'll handle the exception here."

