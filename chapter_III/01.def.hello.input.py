def sayHello(who):
    print('Hi, nice to see you ' + name + '.')

print("Enter your name: \n")
name = input()
sayHello(name)
print(name)
# wywołanie błędu - urgument w nawiasie nie będzie zapamiętany. Nie przypisuje nic do żadnej zmiennej
sayHello(Ala)
print(name)