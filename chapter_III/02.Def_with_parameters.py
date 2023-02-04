def hello(name): # PARAMETER CALLED "NAME"
    print("Hello, " + name)
hello("Alice")
hello("Bob")

## PO WYKONANIU FUNKCI, PARAMETR/ZMIENNA "NAME" BĘDZIE JAKBY ZAPOMNIANY,
## ZMIANNA TA ISTNIEJE TYLKO WEWNĄTRZ FUNKCJI


## DEFINE, CALL, PASS, ARGUMENT, PARAMETER
def sayHello(name): ### DEFINING FUNCTION / CREATING IT
    print("Hello, " + name)
sayHello("Al") ### PASSING STRING TO THE TO THE TOP OF THE FUNCTION

### !!! A value being passed to a function in a function call is an argument.

### To define a function is to create it, just like an assignment statement like spam = 42 creates the spam variable. The def statement defines the sayHello() function ➊. The sayHello('Al') line ➋ calls the now-created function, sending the execution to the top of the function’s code. This function call is also known as passing the string value 'Al' to the function. A value being passed to a function in a function call is an argument. The argument 'Al' is assigned to a local variable named name. Variables that have arguments assigned to them are parameters.
### It’s easy to mix up these terms, but keeping them straight will ensure that you know precisely what the text in this chapter means.