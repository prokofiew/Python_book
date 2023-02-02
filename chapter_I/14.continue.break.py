while True:
    print("who are you")
    name = input()
    if name != "Joe":
        continue
    print("Hello, joe. what is the password")
    password = input()
    if password == "swordfish":
        break
print("Access granted")
