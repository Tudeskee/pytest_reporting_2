from pytest import fixture

# Needed to run a code before each test

@fixture(scope= 'function')
def numbers():
    a = 15
    b = 20
    c = 25
    return [a, b, c]