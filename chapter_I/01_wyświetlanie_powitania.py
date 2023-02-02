# ten program wyświetla powitanie

print("Witaj, Świecie")
print("Jak nasz na imię?")      # prośba o podanie imienia
myName = input()
print("Miło Cię poznać " + myName + ".")
print("LIczba znaków w Twoim imieniu wynosi: ")
print(len(myName))
print("Ile masz lat?")
myAge = input()
print("Za rok będziesz mieć " + str(int(myAge) + 1) + " lat.")
