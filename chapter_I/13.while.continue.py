while True:
    print("Hello, who are you")
    name = input()
    if name != "Filip":
        continue
    print("Hello, Filip. What is the password?")
    password = input()
    if password == "blabla":
        break
print("Acces granted")

