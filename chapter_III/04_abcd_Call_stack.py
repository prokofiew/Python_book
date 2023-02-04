def a():
    print('Starting function a()')
    b()
    d()
    print('Ending function a()')

def b():
    print ('Starting function b()')
    c()
    print('Ending function b()')

def c():
    print('Starting function c()')
    print('Ending function c()')

def d():
    print('Starting function d()')
    print('Ending function d()')

a()
