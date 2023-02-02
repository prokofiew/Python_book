from fileinput import FileInput


# str.format
name = "Filip"
age = 37
profession = "musician"

print("Hello, I'm {}, and I'm {}. I work as a {}." .format(name, age, profession))

# f-strings
myName = "Marek"
myAge = "65"
myProfession = "babysitter"

print(f"hello, {myName}. You are {myAge} and you work as a {myProfession} ")
