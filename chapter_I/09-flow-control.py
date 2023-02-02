from ast import Pass


name = "Filip"
password = "swordfish"
print("Name?")
name = input()
if name == "Filip":
    print("Hello Filip")
else:
    print("Wrong name")
    print("Enter password")
    password = input()
    if password == "swordfish":
        print("acces granted")
    else:
        print("wrong password")
        
        
        
             