import sys
print("Please enter a number")
spam = input()
while True:
    if spam == "1":
        print("Hello")
        break
    elif spam == "2":
        print("Howdy")
        break
    else:
        print("Greetings")
        sys.exit()