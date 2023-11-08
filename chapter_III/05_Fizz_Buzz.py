from ast import Num


print(" Ta funkcja wpisze fizz i buzz oraz fizz buzz w podanym przez Ciebie zakresie liczb")
print()
a = input("Wybierz liczbę a: ")
b = input("Wybierz liczbę b: ")
num = (a, b)

def FizzBuzz(num):
    # myChoice = num in range(int(a), int(b)) 
       
    for num in range(int(a), int(b)):
        if num % 3 == 0 and num % 5 == 0 :
            return "FizzBuzz"
        
        elif num % 3 == 0 :
            return "Fizz"
            
        elif num % 5 == 0 :
            return "Buzz"
        else:
            return num

print (FizzBuzz(num))
