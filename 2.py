import math

while True:
    try:
        number = int(input("Enter a positive integer less than 100: "))
        isinstance(number, int)
        assert(number > 0)
        assert(number < 100)
        break
    except ValueError:
        print("That was no valid number!")
    except AssertionError:
        print("Enter more then 0, less then 100.")

#2a
def factorial(number):
    if number > 1:
       return number*factorial(number-1)
    elif number in (0, 1):
        return 1

print(factorial(number))

#2b
fact = math.factorial(number)
print(fact)
